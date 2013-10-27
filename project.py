
from graphics import *
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

    def hood(self):
        pt1 = Point(138,334)
        head = Circle(pt1,86)
        head.setFill(color_rgb(75,179,188))
        head.draw(win)
        circle = Circle(Point(135,244), 9)
        circle.setFill(GENERAL_YELLOW)
        circle.draw(win)


    def make_face(self):
        pt1 = Point(60,300)
        head = Oval(pt1,Point(220,420))
        head.setFill(DEFAULT_SKIN)
        head.draw(win)

    def make_yellow_stripe(self):
        xy_one, xy_two = Point(60,295), Point(220,400)
        head = Oval(xy_one, xy_two)
        head.setFill(color_rgb(251,217,180))
        head.setWidth(5)
        head.setOutline(GENERAL_YELLOW)
        head.draw(win)

    def closed_eyes(self,inverted = None):
        x_one, x_two = 103, 174
        if inverted == 'invert!': x_one ,x_two = 174,103
        xy_one, xy_two = Point(x_one,321), Point(x_two,350)
        new_line = Line(xy_one, xy_two)
        new_line.draw(win)

    def mouth(self):
        mock_up = Oval(Point(126,369), Point(155,382))
        mock_up.setFill('black')
        mock_up.draw(win)
        circle = Circle(Point(138,388), 10)
        circle.setWidth(0)
        circle.setFill(color_rgb(251,217,180))
        circle.draw(win)
        line = Line(Point(127,384), Point(150,386))
        line.draw(win)

    def body(self):
        pol = Polygon(Point(62,356), Point(48,366), Point(35,383), Point(59,392), Point(67,408), Point(41,411), Point(44,420), Point(84,424), Point(84,356))
        pol.setFill(color_rgb(212,31,64))
        pol.draw(win)
        rec = Rectangle(Point(71,374),Point(202,450))
        rec.setWidth(0)
        rec.setFill(color_rgb(212,31,64))
        rec.draw(win)

    def decoration(self):
        lin = Line(Point(144,420),Point(144,450))
        lin.setWidth(2)
        lin.draw(win)
        y1 = 420
        y2 = 425
        while y1 <= 449:
            lin2 = Line(Point(140,y1), Point(140,y2))
            lin2.setWidth(2)
            lin2.draw(win)
            y1 += 8
            y2 += 8

    def hand(self):
        oval = Oval(Point(27,383), Point(75,417))
        oval.setFill(GENERAL_YELLOW)
        oval.draw(win)
        for each in range(35,65,5):
            lin = Line(Point(each,388), Point(each,400))
            lin.draw(win)

    def low_body(self):
        super(Bob, self).low_body([0]*4, [0]*4, color_rgb(157,95,82))
        super(Bob, self).feet('black')

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

    def hood(self):
        rec = Rectangle(Point(210,269), Point(333,329))
        rec.setFill(color_rgb(34,154,56))
        rec.draw(win)
        rec2 = Rectangle(Point(205,266), Point(341,297))
        rec2.setFill(color_rgb(87,197,38))
        rec2.draw(win)
        oval = Oval(Point(327,298),Point(346,355))
        oval2 = Oval(Point(202,298),Point(223,355))
        for each in [oval, oval2]:
            each.setWidth(0)
            each.setWidth(0)
            each.setFill(color_rgb(87,197,38))
            each.draw(win)

    def head(self):
        self.outerhead()
        super(Nick, self).head()

    def outerhead(self):
        circle = Circle(Point(273,373), 65)
        circle.setFill(color_rgb(34,154,56))
        circle.draw(win)

    def eyes(self):
        x, x2 = 240, 264
        while x <= 296:
            oval = Oval(Point(x,339), Point(x2 ,375))
            oval.setFill('white')
            oval.draw(win)
            x += 30
            x2 += 30
        #inner eyes
        for each in range(256,279,22):
            circle = Circle(Point(each,355),3)
            circle.setFill('black')
            circle.draw(win)

    def decoration(self):
        lin = Line(Point(268,433),Point(268,463))
        lin.setWidth(2)
        lin.draw(win)

    def mouth(self):
        pol = Polygon(Point(255,390), Point(285,389), Point(280,400),Point(263,399))
        pol.setFill('black')
        pol.draw(win)
        self.teeth()

    def teeth(self):
        x1 = 263
        x2 = 267
        while x1 <= 275:
            rec = Rectangle(Point(x1,390),Point(x2,393))
            rec.setFill('white')
            rec.draw(win)
            x1 += 6
            x2 += 6

    def body(self):
        super(Nick, self).body(color_rgb(254,97,16))

    def hands(self):
        super(Nick, self).hands([0], [0], color_rgb(87,197,38))
        super(Nick, self).hands([160], [0], color_rgb(87,197,38))

    def arm(self):
        self.hands()
        super(Nick, self).arm([0]*9,[22]*9, color_rgb(254,97,16))


    def arm_right(self):
        super(Nick, self).arm_right([0]*9,[0]*9, color_rgb(254,97,16))

    def low_body(self):
        super(Nick, self).low_body([150]*4, [10]*4, color_rgb(47,79,76), 30)
        super(Nick, self).feet('black',135,135,10,10)

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

class Carlos(CommomParts):

    def head(self):
        super(Carlos, self).head(150)

    def mohawk(self):
        pol = Polygon(Point(421,249),Point(450,296),Point(421,319),Point(396,297))
        pol.setFill('black')
        pol.draw(win)

    def eyebrow(self):
        lin = Line(Point(377,342), Point(410,350))
        lin2 = Line(Point(430,350),Point(473,342))
        for each in [lin, lin2]:
            each.setWidth(2)
            each.draw(win)

    def eyes(self):
        x = 0
        for each in range(393,439,45):
            x += 1
            print x
            y = (360 if x == 2 else 355)
            cir = Circle(Point(each,y),11)
            cir.setFill('white')
            cir.draw(win)
            cir2 = Circle(Point(each,y),5)
            cir2.setFill('black')
            cir2.draw(win)

    def mouth(self):
        cir = Circle(Point(418,388), 20)
        cir.setFill('black')
        cir.draw(win)
        cir1 = Circle(Point(417,383), 20)
        cir1.setFill(DEFAULT_SKIN)
        cir1.setWidth(0)
        cir1.draw(win)

    def decoration(self):
        lin = Line(Point(420,433),Point(420,463))
        lin.setWidth(2)
        lin.draw(win)
        rec = Rectangle(Point(420,433),Point(430,443))
        rec.draw(win)

    def arm(self):
        super(Carlos, self).arm([163]*9,[30]*9,color_rgb(157,95,82))

    def arm_right(self):
        super(Carlos, self).arm_right([150]*9,[10]*9,color_rgb(157,95,82))

    def body(self):
        super(Carlos, self).body(color_rgb(157,95,82),150)

    def hands(self):
        super(Carlos, self).hands([170], [10], color_rgb(212,31,64))
        super(Carlos, self).hands([300], [10], color_rgb(212,31,64))

    def low_body(self):
         super(Carlos, self).low_body([300]*4, [10]*4, color_rgb(80,98,162), 30)
         super(Carlos, self).feet(color_rgb(212,31,64),285,285,10,10)

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


new_bob = Bob()
new_bob.draw_self()

new_carlos = Carlos()
new_carlos.draw_self()

new_nick = Nick()
new_nick.draw_self()

