from graphics import *
from random import *
from time import sleep

win = GraphWin("The Family", 900, 506)

GENERAL_YELLOW = color_rgb(249,221,4)
DEFAULT_SKIN = color_rgb(251,217,180)

"""
The Family

Documentation and Understanding :

There are 3 characters, they have their own characteristics and some that are shared.
They will be instatiated at the bottom of the file, calling the draw_self function

You can check the code out on GitHub : https://github.com/vaot/various/blob/master/project.py

1 - Parent Class

    * Provide all the commom characteristics among them

    * All methods are scalable in terms of X and Z in the coordinate
    * meaning that each feature can be scaled to fit and be placed at the right
    * spot in the board.

    * Most of all features provide the scalability through an array
    * and the length of that array will depend on the feature
    * Child classes (each character) will then implement its own feature
    * inheriting from the super class('Parent') and specifing the scalability(Xs,Ys) in the board

2 - Child Classes (Bob, Nick, Carlos)

    * They will all have their features
    * and provide the right scalability values for those
    * who are shared among them

    * Each child provide draw_'child_name' function
    * that function will be responsible for order of execution

"""

class Background(object):
    
    def floor(self):
        self.snow()
        rec = Rectangle(Point(0,400),Point(900,506))
        rec.setFill('white')
        rec.setWidth(0)
        rec.draw(win)
        
    def snow(self):
        x1 = 0
        x2 = 100
        while x1 <= 900:
            oval = Oval(Point(x1,380),Point(x2,420))
            oval.setFill('white')
            oval.draw(win)
            x1 += 100
            x2 += 100
    
    def moutains(self):
        x1,x2,x3,ymid = 0, 200, 400,10
        while x1 <= 800:
             pol = Polygon(Point(x1,420),Point(x2,ymid),Point(x3,420))
             pol.setFill(color_rgb(18,114,5))
             pol.draw(win)
             x1 += 400
             x2 += 400
             x3 += 400
             ymid += 100

    def make_snow(self):
        x = 150
        y = 10
        while x <= 400:
            pt = Circle(Point(x,y),10)
            pt.setFill('white')
            pt.draw(win)
            x += 30
            y = y + ((15*5)/2)*2
            
    def top_snow(self):
        pol = Polygon(Point(602,104),Point(552,183),Point(575,160),Point(580,183),Point(605,160),Point(656,183))
        pol.setFill('white')
        pol.draw(win)

    def draw_self(self):
        self.moutains()
        self.top_snow()
        self.make_snow()
        self.floor()
             
        
class Parent(object):

    def arm(self, array, array2, color):
        pol = Polygon(Point(array[0] + 202, array2[0] + 356),
                      Point(array[1] + 188,array2[1] + 366),
                      Point(array[2] + 175,array2[2] + 383),
                      Point(array[3] + 199,array2[3] + 392),
                      Point(array[4] +207,array2[4] + 408),
                      Point(array[5] + 181,array2[5] + 411),
                      Point(array[6] + 184,array2[6] + 420),
                      Point(array[7] + 224,array2[7] + 424),
                      Point(array[8] + 244,array2[8] + 436))

        pol.setFill(color)
        pol.setWidth(0)
        pol.draw(win)

    def arm_right(self, array, array2, color):
        pol = Polygon(Point(318 + array[0],353 + array2[0]),
                      Point(350 + array[1],411 + array2[1]),
                      Point(350 + array[2],434 + array2[2]),
                      Point(315 + array[3],450 + array2[3]))

        pol.setFill(color)
        pol.draw(win)

    def hands(self, array , array2, color):
        circle = Circle(Point(187 + array[0],
                              420 + array2[0]),20)
        circle.setFill(color)
        circle.draw(win)
        min_c = Circle(Point(196 + array[0],409 + array2[0]), 6)
        min_c.setFill(color)
        min_c.setWidth(2)
        min_c.draw(win)

    def head(self, scalex = 0, scaley = 0):
        circle = Circle(Point(273 + scalex,363 + scaley), 70)
        circle.setFill(DEFAULT_SKIN)
        circle.draw(win)

    def body(self, color, scalex = 0, scaley = 0):
        rec = Rectangle(Point(222 + scalex,394 + scaley), Point(322 + scalex , 462 + scaley))
        rec.setFill(color)
        rec.setWidth(0)
        rec.draw(win)

    def low_body(self, array1, array2, color, scale_size = 0):
        pol = Polygon(Point(77 + array1[0],444 + array2[0]),
                      Point(200 + array1[1] - scale_size,444 + array2[1]),
                      Point(193 + array1[2] - scale_size, 462 + array2[2]),
                      Point(80 + array1[3], 462 + array2[3]))

        pol.setFill(color)
        pol.draw(win)

    def feet(self, color, scalex = 0, scalex2 = 0, scaley = 0, scaley2 = 0):
        limit = 128 + scalex
        x1,x2 = (83 + scalex), (141 + scalex2)
        while x1 <= limit:
            print x1, x2
            oval = Oval(Point(x1, 461 + scaley),Point(x2, 475 + scaley2))
            oval.setFill(color)
            oval.draw(win)
            x1 += 45
            x2 += 45

class Bob(Parent):
    
    def __init__(self, scalex):
        self.scalex = scalex
        
    def hood(self):
        pt1 = Point(138 + self.scalex,334)
        head = Circle(pt1,86)
        head.setFill(color_rgb(75,179,188))
        head.draw(win)
        circle = Circle(Point(135 + self.scalex,244), 9)
        circle.setFill(GENERAL_YELLOW)
        circle.draw(win)


    def make_face(self):
        pt1 = Point(60 + self.scalex,300)
        head = Oval(pt1,Point(220 + self.scalex,420))
        head.setFill(DEFAULT_SKIN)
        head.draw(win)

    def make_yellow_stripe(self):
        xy_one, xy_two = Point(60 + self.scalex,295), Point(220 + self.scalex,400)
        head = Oval(xy_one, xy_two)
        head.setFill(color_rgb(251,217,180))
        head.setWidth(5)
        head.setOutline(GENERAL_YELLOW)
        head.draw(win)

    def closed_eyes(self,inverted = None):
        x_one, x_two = 103  + self.scalex, 174 + self.scalex
        if inverted == 'invert!': x_one ,x_two = 174 + self.scalex ,103 + self.scalex
        xy_one, xy_two = Point(x_one,321), Point(x_two,350)
        new_line = Line(xy_one, xy_two)
        new_line.draw(win)

    def mouth(self):
        mock_up = Oval(Point(126 + self.scalex,369), Point(155 + self.scalex,382))
        mock_up.setFill('black')
        mock_up.draw(win)
        circle = Circle(Point(138 + self.scalex,388), 10)
        circle.setWidth(0)
        circle.setFill(color_rgb(251,217,180))
        circle.draw(win)
        line = Line(Point(127 + self.scalex,384), Point(150 + self.scalex,386))
        line.draw(win)

    def body(self):
        pol = Polygon(Point(62 + self.scalex,356),
                      Point(48 + self.scalex,366),
                      Point(35 + self.scalex,383),
                      Point(59 + self.scalex,392),
                      Point(67 + self.scalex,408),
                      Point(41 + self.scalex,411),
                      Point(44 + self.scalex,420),
                      Point(84 + self.scalex,424),
                      Point(84 + self.scalex,356))
        
        pol.setFill(color_rgb(212,31,64))
        pol.draw(win)
        rec = Rectangle(Point(71 + self.scalex,374),Point(202 + self.scalex,450))
        rec.setWidth(0)
        rec.setFill(color_rgb(212,31,64))
        rec.draw(win)

    def decoration(self):
        lin = Line(Point(144 + self.scalex,420),Point(144 + self.scalex,450))
        lin.setWidth(2)
        lin.draw(win)
        y1 = 420
        y2 = 425
        while y1 <= 449:
            lin2 = Line(Point(140 + self.scalex,y1), Point(140 + self.scalex,y2))
            lin2.setWidth(2)
            lin2.draw(win)
            y1 += 8
            y2 += 8

    def hand(self):
        oval = Oval(Point(27 + self.scalex,383), Point(75 + self.scalex,417))
        oval.setFill(GENERAL_YELLOW)
        oval.draw(win)
        for each in range(35,65,5):
            lin = Line(Point(each + self.scalex,388), Point(each + self.scalex,400))
            lin.draw(win)

    def low_body(self):
        super(Bob, self).low_body([0 + self.scalex]*4, [0]*4, color_rgb(157,95,82))
        super(Bob, self).feet('black', self.scalex, self.scalex)

    def draw_self(self):
        self.low_body()
        self.body()
        self.hand()
        self.hood()
        self.make_yellow_stripe()
        self.make_face()
        self.closed_eyes()
        self.closed_eyes('invert!')
        self.mouth()
        self.decoration()

class Nick(Parent):
    
    def __init__(self, scalex):
        self.scalex = scalex
        
    def hood(self):
        color = color_rgb(randint(0,255),
                          randint(0,255),
                          randint(0,255))
        rec = Rectangle(Point(210 + self.scalex,269), Point(333 + self.scalex,329))
        rec.setFill(color_rgb(34,154,56))
        rec.draw(win)
        rec2 = Rectangle(Point(205 + self.scalex,266), Point(341 + self.scalex,297))
        rec2.setFill(color)
        rec2.draw(win)
        oval = Oval(Point(327 + self.scalex,298),Point(346 + self.scalex,355))
        oval2 = Oval(Point(202 + self.scalex,298),Point(223 + self.scalex,355))
        for each in [oval, oval2]:
            each.setWidth(0)
            each.setWidth(0)
            each.setFill(color_rgb(87,197,38))
            each.draw(win)

    def head(self):
        self.outerhead()
        super(Nick, self).head(self.scalex)

    def outerhead(self):
        color = color_rgb(randint(0,255),
                          randint(0,255),
                          randint(0,255))
        circle = Circle(Point(273  + self.scalex,373), 65)
        circle.setFill(color)
        circle.draw(win)

    def eyes(self):
        color = color_rgb(randint(0,255),
                          randint(0,255),
                          randint(0,255))
        x, x2 = 240, 264
        while x <= 296:
            oval = Oval(Point(x + self.scalex,339), Point(x2 + self.scalex ,375))
            oval.setFill(color)
            oval.draw(win)
            x += 30
            x2 += 30
        #inner eyes
        for each in range(256,279,22):
            circle = Circle(Point(each + self.scalex,355),3)
            circle.setFill('black')
            circle.draw(win)
            
    def decoration(self):
        lin = Line(Point(268 + self.scalex,433),Point(268 + self.scalex,463))
        lin.setWidth(2)
        lin.draw(win)

    def mouth(self):
        pol = Polygon(Point(255 + self.scalex,390), Point(285 + self.scalex,389), Point(280 + self.scalex,400),Point(263 + self.scalex,399))
        pol.setFill('black')
        pol.draw(win)
        self.teeth()

    def teeth(self):
        x1 = 263
        x2 = 267
        while x1 <= 275:
            rec = Rectangle(Point(x1 + self.scalex,390),Point(x2 + self.scalex,393))
            rec.setFill('white')
            rec.draw(win)
            x1 += 6
            x2 += 6

    def body(self):
        super(Nick, self).body(color_rgb(254,97,16), self.scalex)

    def hands(self):
        color = color_rgb(randint(0,255),
                          randint(0,255),
                          randint(0,255))
        super(Nick, self).hands([0 + self.scalex], [0], color)
        super(Nick, self).hands([160 + self.scalex], [0], color)

    def arm(self):
        self.hands()
        super(Nick, self).arm([0  + self.scalex]*9,[22]*9, color_rgb(254,97,16))


    def arm_right(self):
        super(Nick, self).arm_right([0 + self.scalex]*9,[0]*9, color_rgb(254,97,16))

    def low_body(self):
        color = color_rgb(randint(0,255),
                          randint(0,255),
                          randint(0,255))
        super(Nick, self).low_body([150  + self.scalex]*4, [10]*4, color, 30)
        super(Nick, self).feet('black',135  + self.scalex,135  + self.scalex,10,10)

    def draw_self(self):
        self.low_body()
        self.arm()
        self.arm_right()
        self.hands()
        self.body()
        self.head()
        self.hood()
        self.eyes()
        self.mouth()
        self.decoration()

class Carlos(Parent):

    def __init__(self, scalex):
        self.scalex = scalex
        
    def head(self):
        super(Carlos, self).head(150 + self.scalex)

    def mohawk(self):
        pol = Polygon(Point(421 + self.scalex,249),
                      Point(450 + self.scalex,296),
                      Point(421 + self.scalex,319),
                      Point(396 + self.scalex,297))
        
        pol.setFill(color_rgb(randint(0,255),
                              randint(0,255),
                              randint(0,255)))
        pol.draw(win)

    def eyebrow(self):
        lin = Line(Point(377 + self.scalex,342), Point(410 + self.scalex,350))
        lin2 = Line(Point(430 + self.scalex,350),Point(473 + self.scalex,342))
        for each in [lin, lin2]:
            each.setWidth(2)
            each.draw(win)

    def eyes(self):
        x = 0
        color = color_rgb(randint(0,255),
                          randint(0,255),
                          randint(0,255))
        for each in range(393,439,45):
            x += 1
            print x
            y = (360 if x == 2 else 355)
            cir = Circle(Point(each + self.scalex,y),11)
            cir.setFill(color)
            cir.draw(win)
            cir2 = Circle(Point(each + self.scalex,y),5)
            cir2.setFill('black')
            cir2.draw(win)

    def mouth(self):
        cir = Circle(Point(418 + self.scalex,388), 20)
        cir.setFill('black')
        cir.draw(win)
        cir1 = Circle(Point(417 + self.scalex,383), 20)
        cir1.setFill(DEFAULT_SKIN)
        cir1.setWidth(0)
        cir1.draw(win)

    def decoration(self):
        lin = Line(Point(420 + self.scalex,433),Point(420 + self.scalex,463))
        lin.setWidth(2)
        lin.draw(win)
        rec = Rectangle(Point(420 + self.scalex,433),Point(430 + self.scalex,443))
        rec.draw(win)

    def arm(self):
        super(Carlos, self).arm([163  + self.scalex]*9,[30]*9,color_rgb(157,95,82))

    def arm_right(self):
        super(Carlos, self).arm_right([150 + self.scalex]*9,[10]*9,color_rgb(157,95,82))

    def body(self):
        super(Carlos, self).body(color_rgb(157,95,82),150 + self.scalex)

    def hands(self):
        color = color_rgb(randint(0,255),
                          randint(0,255),
                          randint(0,255))
        super(Carlos, self).hands([170 + self.scalex], [10], color)
        
        super(Carlos, self).hands([300 + self.scalex], [10], color)

    def low_body(self):
         super(Carlos, self).low_body([300 + self.scalex]*4, [10]*4, color_rgb(randint(0,255),
                                                                 randint(0,255),
                                                                 randint(0,255)), 30)
         super(Carlos, self).feet(color_rgb(randint(0,255),
                                            randint(0,255),
                                            randint(0,255)),
                                            285 + self.scalex,
                                            285  + self.scalex,10,10)

    def draw_self(self):
        self.low_body()
        self.arm()
        self.arm_right()
        self.body()
        self.head()
        self.mohawk()
        self.eyebrow()
        self.eyes()
        self.mouth()
        self.hands()
        self.decoration()



def main():
    img2 = Image(Point(0,150), "airplane (1).gif")
    img2.draw(win)
    
    v = Entry(Point(400,10),400)
    v .setText('Victor Andrey')

    new_ground = Background()
    new_ground.draw_self()


    new_bob = Bob(0)
    new_bob.draw_self()

    new_carlos = Carlos(0)
    new_carlos.draw_self()

    new_nick = Nick(0)
    new_nick.draw_self()

    
    win.setBackground('white')

    for i in range(200):
        img2.move(5,0)
        sleep(.2)
        
    t = Text(Point(800,20),'by vaot')
    t.draw(win)

main()
