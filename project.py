from graphics import *
win = GraphWin("My Circle", 900, 506)

GENERAL_YELLOW = color_rgb(249,221,4)
DEFAULT_SKIN = color_rgb(251,217,180)

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
        
class Nick(object):
    
    def hood(self):
        rec = Rectangle(Point(210,269), Point(333,329))
        rec.setFill(color_rgb(34,154,56))
        rec.draw(win)
        rec2 = Rectangle(Point(205,266), Point(341,297))
        rec2.setFill(color_rgb(87,197,38))
        rec2.draw(win)
        oval = Oval(Point(327,282),Point(346,342))
        oval2 = Oval(Point(202,282),Point(223,342))
        for each in [oval, oval2]:
            each.setWidth(0)
            each.setWidth(0)
            each.setFill(color_rgb(87,197,38))
            each.draw(win)
            
    def head(self):
        circle = Circle(Point(273,363), 70)
        circle.setFill(DEFAULT_SKIN)
        circle.draw(win)

    def draw_nick(self):
        self.head()
        self.hood()

new_bob = Bob()
new_bob.draw_bob()


new_nick = Nick()
new_nick.draw_nick()
