import turtle

turtle.setup(width=600, height=600, startx=0, starty=0)
wn = turtle.Screen()

t = turtle.Turtle()
t.color("green")             # make the turtle green
t.pencolor("blue")           # set the pen color to blue
t.pensize(20)                # make the pen easier to see
t.turtlesize(5)              # make the turtle larger

t.forward(250)
t.left(120)
t.forward(250)

# wn.bye()
# wn.exitonclick() 
