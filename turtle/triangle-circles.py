import turtle
from random import randint
from math import sin

# via http://krazydad.com/tutorials/makecolors.php
def getcolors(frequency, i):
    red   = sin(frequency*i + 0) * 127 + 128;
    green = sin(frequency*i + 2) * 127 + 128;
    blue  = sin(frequency*i + 4) * 127 + 128;
    return [ red, green, blue ]

t = turtle.Turtle()
turtle.colormode(255)
t.speed(0)
t.pensize(2)
width = 700

t.penup()
t.setposition(-width/2, width/2)
t.pendown()

for i in range(123):
    t.pencolor(getcolors(.3, i))
    t.forward(width)
    t.right(123)
    
turtle.done()