import turtle

def quit():
    window.bye()

window = turtle.Screen()
window.listen()
window.onkeypress(quit, "Escape")

t = turtle.Pen()

t.color('#ff0000')

t.fillcolor('#ff0000')
t.begin_fill()

for i in range(4):
    t.forward(500)
    t.left(90)

t.end_fill()

t.forward(300)
t.left(90)
t.forward(300)

t.color('#ffffff')

t.fillcolor('#ffffff')
t.begin_fill()

for i in range(4):
    for j in range(2):
        t.forward(100)
        t.left(90)
    t.forward(100)
    t.right(90)

t.end_fill()

window.mainloop()
