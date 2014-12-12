import turtle
from random import randint

def shape(sides):
    # TODO
        
def set_random_color():
    colors = ['red', 'orange', 'green', 'blue', 'purple']
    t.pencolor(colors[randint(0, len(colors) - 1)])    
 
turtle.setup(width=800, height=1000, startx=0, starty=0)
t = turtle.Turtle()
t.turtlesize(5)
t.pensize(20)
t.color("green")
t.pencolor("blue")

shape(3)
shape(4)
shape(5)
shape(6)
shape(8)
