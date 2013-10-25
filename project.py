from graphics import *
win = GraphWin("My Circle", 900, 506)

GENERAL_YELLOW = color_rgb(249,221,4)


def hood():
    top = Polygon(Point(128,218), Point(138,218), Point(14,211))
    top.setFill(GENERAL_YELLOW)
    top.draw(win)
    pt1 = Point(138,334)
    head = Circle(pt1,86)
    head.setFill(color_rgb(75,179,188))
    head.draw(win)


def make_face():
    pt1 = Point(60,300)
    head = Oval(pt1,Point(220,420))
    head.setFill(color_rgb(251,217,180))
    head.draw(win)

def make_yellow_stripe():
    xy_one, xy_two = Point(60,295), Point(220,400)
    head = Oval(xy_one, xy_two)
    head.setFill(color_rgb(251,217,180))
    head.setWidth(5)
    head.setOutline(GENERAL_YELLOW)
    head.draw(win)

def closed_eyes(inverted = None):
    x_one, x_two = 103, 174
    if inverted == 'invert!': x_one ,x_two = 174,103
    xy_one, xy_two = Point(x_one,321), Point(x_two,350)
    new_line = Line(xy_one, xy_two)
    new_line.draw(win)

def mouth():
    mock_up = Oval(Point(126,369), Point(155,382))
    mock_up.setFill('black')
    mock_up.draw(win)
    circle = Circle(Point(138,388), 10)
    circle.setWidth(0)
    circle.setFill(color_rgb(251,217,180))
    circle.draw(win)
    line = Line(Point(127,384), Point(150,386))
    line.draw(win)


hood()
make_yellow_stripe()
make_face()
closed_eyes()
closed_eyes('invert!')
mouth()