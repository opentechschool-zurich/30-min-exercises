import turtle
import math

def quit():
    window.bye()

window = turtle.Screen()
window.listen()
window.onkeypress(quit, "Escape")

black = '#000000'
white = '#ffffff'
green = '#007a4d'
gold = '#ffb612'
red = '#de3831'
blue = '#002395'
# 450 x 300
# stripes: 5:1:3:1:5 (20 * 15)

t = turtle.Pen()

t.speed(10)

def draw_rect(w, h, color):
        t.color(color)
        t.fillcolor(color)
        t.begin_fill()

        for width in [w, h] * 2:
            t.forward(width)
            t.left(90)

        t.end_fill()

def move_down(y):
    """ assumes the cursor is looking to the right"""
    t.penup()
    t.right(90)
    t.forward(y)
    t.left(90)
    t.down()

def move_up(y):
    """ assumes the cursor is looking to the right"""
    t.penup()
    t.left(90)
    t.forward(y)
    t.right(90)
    t.down()

def move_right(y):
    t.forward(y)

def move_left(y):
    t.left(180)
    t.forward(y)
    t.left(180)

def draw_triangle(w, h, color):
    t.color(color)
    t.fillcolor(color)
    direction = t.heading()
    x, y = t.position()

    t.begin_fill()

    t.goto(x + w, y + (h // 2))
    t.goto(x, y + h)

    t.end_fill()

    t.goto(x, y)
    t.setheading(direction)
    t.end_fill()

draw_rect(450, 100, red)
move_down(200)
draw_rect(450, 100, blue)

draw_rect(80, 300, white)
move_right(80)
draw_triangle(240, 300, white)
move_left(80)

move_up(120)
draw_rect(450, 60, green)
move_down(120)
draw_rect(40, 300, green)
move_right(40)
draw_triangle(240, 300, green)
move_left(40)

move_up(40)
draw_triangle(180, 220, gold)

move_up(30)
draw_triangle(140, 160, black)

window.mainloop()
