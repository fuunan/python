import turtle

turtle.setup(800, 600)
turtle.pensize(2)
turtle.pencolor('black')
for i in range(7):
    if i < 3:
        turtle.fd(200)
        turtle.left(120)
    elif i < 5:
        turtle.fd(100)
        turtle.left(120)
    else:
        turtle.left(120)
        turtle.fd(100)
        turtle.left(120)
turtle.done()
