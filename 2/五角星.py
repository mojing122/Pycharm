import turtle as t
t.fillcolor("red")
t.begin_fill()
t.shape("turtle")
t.penup()
t.goto(-150,100)
t.pendown()
for i in range(5):
    t.forward(100)
    t.left(72)
    t.forward(100)
    t.right(144)
t.end_fill()
done()