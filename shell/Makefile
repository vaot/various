## This is a simple Makefile with lost of comments
## Check Unix Programming Tools handout for more info.

# Define what compiler to use and the flags.
CC=cc
CXX=CC
CCFLAGS= -g -std=c99 -Wall -Werror


all: shell test

%.o : %.c
	$(CC) -c $(CCFLAGS) $<

shell: shell.o
	$(CC) -o shell shell.o

test: shell
	./shell

clean:
	rm -f core *.o shell

