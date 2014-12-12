import random

max = 10

num = int(random.random() * max + 1)
name = raw_input("What's your name? ")

print "Nice to meet you, %s" % name
print "I've chosen a number from 1 to 10, try to guess it."
print

guess = 0
tries = 0

while guess != num:
    
    try:
        guess = int(raw_input("Enter your guess (1 to %d): " % max))
    except ValueError:
        print "Whoops, that's not a number"

    tries += 1
    
    if guess < num:
        print "Higher"
        
    elif guess > num:
        print "Lower"
    
    else:
        print "Nice work %s, you guessed it in %d tries!" % (name, tries)