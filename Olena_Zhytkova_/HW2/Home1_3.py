import turtle
turtle.up()
turtle.goto(0,-100)
turtle.down()
turtle.begin_fill()
turtle.fillcolor('yellow')
turtle.circle(100)
turtle.end_fill()

turtle.up()
turtle.goto(-69,-40)
turtle.width(5)
turtle.setheading(-60)
turtle.down()
turtle.circle(80,120)
turtle.fillcolor('black')

for i in range(-35,105,70):
    turtle.up()
    turtle.goto(i,10)
    turtle.down()
    turtle.setheading(0)
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()



turtle.done()
