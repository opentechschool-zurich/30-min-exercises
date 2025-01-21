import turtle

def quit():
    window.bye()

window = turtle.Screen()
window.listen()
window.onkeypress(quit, "Escape")

t = turtle.Pen()

# 1:1.6
# 10:16
# 5:8
# 30:48
# 300:480

# t.speed(10)

t.color('#6cace4')


for i in range(2):
    t.fillcolor('#6cace4')
    t.begin_fill()

    for width in [480, 100] * 2:
        t.forward(width)
        t.left(90)

    t.end_fill()

    if i == 0:
        t.penup()
        t.right(90)
        t.forward(200)
        t.left(90)
        t.down()

t.penup()

t.forward(200)
t.left(90)
t.forward(145)
t.right(90)
t.pendown()

t.color('red', 'yellow')
t.begin_fill()

for i in range(36):
    t.forward(100)
    t.left(170)

t.end_fill()

window.mainloop()
