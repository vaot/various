#define _BSD_SOURCE
#define _XOPEN_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <string.h>
#include <stdbool.h>
#include <unistd.h>
#include <errno.h>
#include <signal.h>
#include <sys/wait.h>

#define COMMAND_LENGTH 1024
#define NUM_TOKENS (COMMAND_LENGTH / 2 + 1)
#define HISTORY_DEPTH 10


/* Variable used for history feature. commandCursor points to the location of
* the current command in the circular array. commandCounter is the number of
* total commands run.
*/
char history[HISTORY_DEPTH][COMMAND_LENGTH];
int commandCursor = 0;
int commandCounter = 0;

/* End of Medium Value*/
const int EM_VALUE = 25;


/**
 * Command Input and Processing
 */

/*
 * Tokenize the string in 'buff' into 'tokens'.
 * buff: Character array containing string to tokenize.
 *       Will be modified: all whitespace replaced with '\0'
 * tokens: array of pointers of size at least COMMAND_LENGTH/2 + 1.
 *       Will be modified so tokens[i] points to the i'th token
 *       in the string buff. All returned tokens will be non-empty.
 *       NOTE: pointers in tokens[] will all point into buff!
 *       Ends with a null pointer.
 * returns: number of tokens.
 */
int tokenize_command(char *buff, char *tokens[]);

/*
* Handles making a copy of the command from the history
* tokenizing it and cleaning up the tmp copy.
* The copy is required since #tokenize_command() will change
* the value of the command, by separating args with a '/0'.
*/
void retokenize_cmd(int cmdPosition, char *tokens[], char *bufCopy, char *buff, _Bool *in_bg);

/**
 * Read a command from the keyboard into the buffer 'buff' and tokenize it
 * such that 'tokens[i]' points into 'buff' to the i'th token in the command.
 * buff: Buffer allocated by the calling code. Must be at least
 *       COMMAND_LENGTH bytes long.
 * tokens[]: Array of character pointers which point into 'buff'. Must be at
 *       least NUM_TOKENS long. Will strip out up to one final '&' token.
 *       tokens will be NULL terminated (a NULL pointer indicates end of tokens).
 * in_background: pointer to a boolean variable. Set to true if user entered
 *       an & as their last token; otherwise set to false.
 */
char* read_command(char *buff, char *tokens[], _Bool *in_background, int *token_count);

void extract_background_arg(int token_count, char *tokens[], _Bool *in_background);

void print_history();

void handle_SIGINT(int st);

void handle_child(char *tokens[], _Bool in_background);

void handle_parent(pid_t pid, _Bool in_background, char *tokens[]);

void handle_fork(pid_t pid, _Bool in_background, char *tokens[]);

int handle_inline_commands(char *tokens[], char *bufCopy, char *buff, _Bool *in_bg);

void add_to_history(char *bufCopy);

int cmd_number_to_position(int cmdNumber);

/**
 * Main and Execute Commands
 */
int main(int argc, char* argv[]) {
  char input_buffer[COMMAND_LENGTH];
  char *tokens[NUM_TOKENS];
  char currentDir[COMMAND_LENGTH];

  struct sigaction handler;
  handler.sa_handler = handle_SIGINT;
  sigaction(SIGINT, &handler, NULL);

  while (true) {
    getcwd(currentDir, sizeof(currentDir));

    // Use write because we need to use read() to work with
    // signals, and read() is incompatible with printf().
    write(STDOUT_FILENO, currentDir, strlen(currentDir));
    write(STDOUT_FILENO, ">", strlen(">"));

    _Bool in_background = false;
    int token_count = 0;

    char *bufCopy = read_command(input_buffer, tokens, &in_background, &token_count);

    // Cmd was invalid, or it was part of the Ctr+C signal.
    // Nothing was copied, and therefore there is nothing to be run.
    if (bufCopy == NULL) {
      continue;
    }

    int handledInline = handle_inline_commands(tokens, bufCopy, input_buffer, &in_background);
    // Cmd was handled by the inline command handler.
    if (handledInline != 0) {
      continue;
    }

    pid_t pid = fork();
    handle_fork(pid, in_background, tokens);
    add_to_history(bufCopy);

    // Cleanup any previously exited background child processes
    // (The zombies)
    while (waitpid(-1, NULL, WNOHANG) > 0);
  }

  return 0;
}

void add_to_history(char *bufCopy) {
  strcpy(history[commandCursor], bufCopy);
  commandCursor = (commandCursor + 1) % HISTORY_DEPTH;
  commandCounter++;
  free(bufCopy);
}

char* read_command(char *buff, char *tokens[], _Bool *in_background, int *token_count) {
  *in_background = false;

  // Read input
  int length = read(STDIN_FILENO, buff, COMMAND_LENGTH-1);

  if ((length < 0) && (errno !=EINTR) ){
    perror("Unable to read command. Terminating.\n");
    exit(-1);  /* terminate with error */
  }

  if ((length < 0) && (errno ==EINTR)){
    buff[0] = '\0';
    return NULL;
  }

  // Null terminate and strip \n.
  buff[length] = '\0';
  if (buff[strlen(buff) - 1] == '\n') {
    buff[strlen(buff) - 1] = '\0';
  }

  char *copy = malloc(sizeof(buff));
  strcpy(copy, buff);

  // Tokenize (saving original command string)
  *token_count = tokenize_command(buff, tokens);

  if (*token_count == 0) {
    free(copy);
    return NULL;
  }

  // Extract if running in background:
  extract_background_arg(*token_count, tokens, in_background);

  return copy;
}

int tokenize_command(char *buff, char *tokens[]) {
  int token_count = 0;
  _Bool in_token = false;
  int num_chars = strnlen(buff, COMMAND_LENGTH);

  for (int i = 0; i < num_chars; i++) {
    switch (buff[i]) {
    // Handle token delimiters (ends):
    case ' ':
    case '\t':
    case '\n':
      buff[i] = '\0';
      in_token = false;
      break;

    // Handle other characters (may be start)
    default:
      if (!in_token) {
        tokens[token_count] = &buff[i];
        token_count++;
        in_token = true;
      }
    }
  }

  if (token_count != 0) {
    tokens[token_count] = NULL;
  }

  return token_count;
}

void print_history() {
  if (commandCounter == 0) {
    return;
  }

  if (commandCounter > HISTORY_DEPTH) {
    int pass = commandCounter/HISTORY_DEPTH;

    if (commandCursor > 0) {
      for (int i = commandCursor; i < HISTORY_DEPTH; ++i) {
        if (strlen(history[i]) == 0) continue;
        printf("%i\t%s\n", ((pass-1)*10) + (i+1), history[i]);
      }

      for (int i = 0; i < commandCursor; ++i){
        printf("%i\t%s\n", ((pass)*10) + (i+1), history[i]);
      }
    } else {
      printf("%i\t%s\n", (commandCounter+1) - HISTORY_DEPTH, history[0]);

      for (int i = 1; i < HISTORY_DEPTH; ++i)
      {
        printf("%i\t%s\n", (((pass)*10) + (i+1))-HISTORY_DEPTH, history[i]);
      }
    }
    return;
  }

  if (commandCursor > 0) {
    for (int i = commandCursor; i < HISTORY_DEPTH; ++i) {
      if (strlen(history[i]) == 0) continue;
      printf("%i\t%s\n", i+1, history[i]);
    }

    for (int i = 0; i < commandCursor; ++i){
      printf("%i\t%s\n", i+1, history[i]);
    }
  } else {
    for (int i = 0; i < HISTORY_DEPTH; ++i)
    {
      printf("%i\t%s\n", i+1, history[i]);
    }
  }
}

void handle_SIGINT(int st) {
  printf("\n");
  print_history();
}

void handle_child(char *tokens[], _Bool in_background) {
  if (in_background) {
    write(STDOUT_FILENO, "\n", 1);
  }

  execvp(tokens[0], tokens);

  /* If we are here that's because execvp failed */
  printf("%s: Unknown command.\n", tokens[0]);
  exit(-1);
}

void handle_parent(pid_t pid, _Bool in_background, char *tokens[]) {
  if (!in_background){
    int status;
    waitpid(pid, &status, 0);
  }
}

void handle_fork(pid_t pid, _Bool in_background, char *tokens[]) {
  if (pid == 0) {
    handle_child(tokens, in_background);
  } else if (pid < 0) {
    fprintf(stderr, "Please, make sure to specify a positive integer.\n");
  } else {
    handle_parent(pid, in_background, tokens);
  }
}

int cmd_number_to_position(int cmdNumber) {
  int cmdLocation = cmdNumber;

  if (cmdNumber > HISTORY_DEPTH) {
    int pass = commandCounter/HISTORY_DEPTH;
    cmdLocation = (cmdLocation - (pass*10));
  }

  return cmdLocation-1;
}

int handle_inline_commands(char *tokens[], char *bufCopy, char *buff, _Bool *in_bg) {
  int reply = 0;

  if (strcmp(tokens[0], "exit") == 0) {
    reply = 1;
    free(bufCopy);
    exit(0);
  } else if (strcmp(tokens[0], "cd") == 0) {
    chdir(tokens[1]);
    add_to_history(bufCopy);
    reply = 1;

  } else if (strcmp(tokens[0], "pwd") == 0) {
    char dir[COMMAND_LENGTH];
    getcwd(dir, sizeof(dir));
    dir[strlen(dir)] = '\0';

    write(STDOUT_FILENO, dir, strlen(dir));
    write(STDOUT_FILENO, "\n", strlen("\n"));
    add_to_history(bufCopy);
    reply = 1;

  } else if (strcmp(tokens[0], "history") == 0) {
    add_to_history(bufCopy);
    print_history();
    reply = 1;

  } else if (strcmp(tokens[0], "!!") == 0) {
    if (commandCounter <= 0) {
      printf("SHELL: Unknown history command.\n");
      free(bufCopy);
      reply = -1;
    } else {
      retokenize_cmd(commandCursor-1, tokens, bufCopy, buff, in_bg);
      printf("%s\n", bufCopy);

      // Recurse, in case the command is to be handled
      // inline.
      reply = handle_inline_commands(tokens, bufCopy, buff, in_bg);
    }

  } else if (tokens[0][0] == '!') {
    int count = strlen(tokens[0]);

    for (int i = 0; i < count-1; ++i) tokens[0][i] = tokens[0][i+1];
    tokens[0][count-1] = '\0';

    int cmdNumber = atoi(tokens[0]);

    if (cmdNumber > commandCounter) {
      printf("SHELL: Unknown history command.\n");
      free(bufCopy);
      reply = -1;

    } else if (cmdNumber == 0) {
      printf("SHELL: Unknown history command.\n");
      free(bufCopy);
      reply = -1;

    } else {
      int cmdPosition = cmd_number_to_position(cmdNumber);
      retokenize_cmd(cmdPosition, tokens, bufCopy, buff, in_bg);
      printf("%s\n", bufCopy);

      // Recurse, in case the command is to be handled
      // inline.
      reply = handle_inline_commands(tokens, bufCopy, buff, in_bg);
    }


  } else if ((int)(*tokens[0]) == EM_VALUE) {
    free(bufCopy);
    reply = -1;

  /* Handle when they type a bunch of spaces and hit enter */
  } else if (strlen(*tokens) == 0) {
    free(bufCopy);
    reply = -1;

  } else {
    reply = 0;
  }

  return reply;
}

void extract_background_arg(int token_count, char *tokens[], _Bool *in_background) {
  if (token_count > 0 && strcmp(tokens[token_count - 1], "&") == 0) {
    *in_background = true;
    tokens[token_count - 1] = 0;
  }
}

void retokenize_cmd(int cmdPosition, char *tokens[], char *bufCopy, char *buff, _Bool *in_bg) {
  strcpy(buff, history[cmdPosition]);
  strcpy(bufCopy, buff);

  int token_count = tokenize_command(buff, tokens);
  extract_background_arg(token_count, tokens, in_bg);
}
