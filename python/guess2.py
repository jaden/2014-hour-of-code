from random import randint

answer = randint(1,100)

guess = 0
tries = 0

while guess != answer:
    guess = int(raw_input("Guess a number from 1 to 100: "))
    tries += 1

    if guess < answer:
        print "Too low"
    elif guess > answer:
        print "Too high"
    
print "Correct, you guessed it in %d tries" % tries


