from graphics import *
win = GraphWin("My Circle", 900, 506)

GENERAL_YELLOW = color_rgb(249,221,4)
DEFAULT_SKIN = color_rgb(251,217,180)

class CommomParts(object):

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

        
class Bob(object):
    
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

    def hand(self):
        oval = Oval(Point(27,383), Point(75,417))
        oval.setFill(GENERAL_YELLOW)
        oval.draw(win)
        for each in range(35,65,5):
            lin = Line(Point(each,388), Point(each,400))
            lin.draw(win)

    def draw_bob(self):
        self.body()
        self.hand()
        self.hood()
        self.make_yellow_stripe()
        self.make_face()
        self.closed_eyes()
        self.closed_eyes('invert!')
        self.mouth()
        
class Nick(CommomParts):
    
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
        circle = Circle(Point(273,363), 70)
        circle.setFill(DEFAULT_SKIN)
        circle.draw(win)
        
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
        rec = Rectangle(Point(222,394), Point(322, 462))
        rec.setFill(color_rgb(254,97,16))
        rec.setWidth(0)
        rec.draw(win)
        
    def hands(self):
        super(Nick, self).hands([0], [0], color_rgb(87,197,38))
        super(Nick, self).hands([160], [0], color_rgb(87,197,38))
        
    def arm(self):
        # Now all we have to do is scale the arm
        # In other words, every single x or y will be multiplied by
        # the number in th array
        self.hands()
        super(Nick, self).arm([0]*9,[22]*9, color_rgb(254,97,16))
    

    def arm_right(self):
        super(Nick, self).arm_right([0]*9,[0]*9, color_rgb(254,97,16))
        
    def draw_nick(self):
        self.arm()
        self.arm_right()
        self.hands()
        self.body()
        self.head()
        self.hood()
        self.eyes()
        self.mouth()        

new_bob = Bob()
new_bob.draw_bob()


new_nick = Nick()
new_nick.draw_nick()
