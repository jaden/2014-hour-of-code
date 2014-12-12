from random import randint

name = raw_input("What is your name? ")
print "Hi %s" % name

answer = raw_input("Want to play a game? (y/n) ")
if answer == 'n':
	print "Maybe some other time"
	exit()

number = randint(1,100)

guess = 0
tries = 0

while guess != number:
	guess = int(raw_input("Guess a number from 1 to 100: "))
	if guess < number:
		print "Too low"
	elif guess > number:
		print "Too high"
	tries += 1

print "Congratulations! You guessed it in %d tries" % tries