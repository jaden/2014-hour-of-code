# Hour of Code

The code and lesson outline I created to do the Hour of Code 2014 with my kids' 3rd and 4th grade classes.

## Suggested Software

- Python (obviously)
- [ZoomIt](http://technet.microsoft.com/en-us/sysinternals/bb897434.aspx)
- IDLE for code editing (comes with Python)

### Required Python modules

- textblob
- nltk
- matplotlib (included with Portable Python)
- numpy (included with Portable Python)

## Classroom Setup

I installed [Portable Python](http://portablepython.com) on a USB flash drive and plugged it into the teacher's Windows desktop.

- Open IDLE and set font size 20 and bold font so class can read the text
- Run ZoomIt and accept the license agreement. Ctrl+1, then 'w' to set the screen white and 't' to type Hour of Code, just to be fancy. Could even set the countdown timer.
    
## Zoomit shortcuts
    LiveZoom    - Ctrl-4 (same to exit)
    Zoom In/Out - Ctrl-Up/Ctrl-Down (in zoom mode)
    Draw Mode   - Ctrl-2 (Esc to exit)
        Arrow       - Ctrl+Shift
        Ellipse     - Tab
        Rectangle   - Ctrl
        Line        - Shift
        Colors      - r(ed), g(reen), b(lue), o(range), y(ellow), p(ink)
        Text        - t (Esc or mouse click to exit)
        Erase all   - e
        Undo        - Ctrl-Z
        Pen width   - Ctrl-Up/Ctrl-Down (or mouse wheel) in draw mode
    White/black - w = white, k = black    
    
## Introduction - 5 minutes

How I got started - working through a BASIC manual that came with my family's ADAM Colecovision. Making games on my TI-85 graphing calculator.

Program = instructions for a computer, like a recipe.
Software = a collection of programs

Why learn computer programming?
    Creativity, reasoning, and problem solving. You can create something from nothing.
    It's fun and the skills you learn will help in school but also in your job, even if you don't use computers. Logic, debugging, problem analysis are all essential skills.

Languages = just like English, Spanish and German, there's Python, Javascript, Java, Ruby, C++

[Code.org](http://code.org) - We won't be using it today, but try it at home

We'll be using Python, freely available at [Python.org](http://python.org).

Any questions? Ask them throughout the hour if you have them.

## The Basics - 25 minutes

Run Python IDLE - we are the boss of the computer, it has to do what we say.

### Output
    
	print "hello"
    
### Basic math (+, -, * and /)
    
	2 + 2    
    
    from math import *
    pi
        
### Variables

They're like labels on a box

    x = 2
    x + 2
    
    x = 3
    x + 2
    
Strings too

    name = raw_input("What's your name?")
    print "Nice to meet you, %s"
    
Counting manually
    
	print 1
    print 2
    print 3
    print 4
    print 5
	...
(But that's a pain)
    
### Loops
    
Count to 10 with loops, explaining about 0-indexing and the way range works. Show them output of just range(10), then range(1,11).

    range(10)
    range(1,11)
    
    for i in range(1, 11):
        print i
    
### Functions
    
	def count_to_ten():
        for i in range(1, 11):
            print i

Or more generically:

	def count(n):
		for i in range(1, n + 1):
			print i

### Logic

**If**

    weekday = True
    
    if weekday:
        print "Go to school"
    else:
        print "Play outside"

**While**

    tired = True
    
    while tired:
        print "Sleep"
        tired = False

	print "Now I'm well rested"

### Putting it all together

Write a guessing game together from scratch
    
	from random import randint
	
	number = randint(1, 10)
	guess = 0
	
	while guess != number:
	    guess = int(raw_input("Guess a number from 1 to 10: "))
	    if guess < number:
	        print "Too low"
	    elif guess > number:
	        print "Too high"
	
	print "That's right, the number was %d" % number

## Drawing with Turtle - 10 minutes

Start in IDLE so they can see what happens after each line
    
	import turtle
	
	turtle.setup(width=600, height=600, startx=0, starty=0)
	wn = turtle.Screen()
	
	t = turtle.Turtle()
	t.turtlesize(5)              # make the turtle larger
	t.pensize(20)                # make the pen easier to see
	t.color("green")             # make the turtle green
	t.pencolor("blue")           # set the pen color to blue
	
	t.position()


shape.py (have them help you fill in the shape method)

	def shape(sides):
	    set_random_color()
	    for i in range(1, sides + 1):
	        t.forward(200)
	        t.left(360 / sides)

Names of polygons

- 5 - pentagon
- 6 - hexagon
- 7 - heptagon
- 8 - octagon
- 9 - nonagon
- 10 - decagon 

## Final project - 20 minutes    

Fourth grade class - Parts of Speech and Name charts

Third grade class - Math quiz and times table

### Parts of Speech

Programming not just for art and math - useful for language too.

From sentence_diagramming.py

	from textblob import TextBlob
	
	tb = TextBlob('The red car drove slowly down the street')
	print tb.tags

Show them how simple sentence_diagramming.py code is, have them come up with their own sentences.

## Name charts (plotting)

Run a few examples to show them a few plots, like pie.py, xkcd.py and surface3d.py (you can rotate it with the mouse).

Then run through names.py code briefly, just to get a general idea of how it works.

The kids love to see their names graphed.

- Frank - huge spike in 1998
- Adolf - dropped in 1940s. Can anyone guess why?
- Walter - interesting

Graphs can be deceiving - pay attention to the scale on the left side. And popular != better. I like rare names.

## Math quiz

Create a simple math quiz with them.

	from random import randint

	x = randint(1, 12)
	y = randint(1, 12)
	
	answer = x / y
	
	your_answer = int(raw_input("What is %d / %d? " % (x, y)))
	
	if answer == your_answer:
	    print "Correct!"
	else:
	    print "Whoops, the answer is: %d" % answer

## Times Table

Show them the output of times_table.py and change the low and high values. Walk them through the code.

