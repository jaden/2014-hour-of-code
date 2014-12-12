from random import randint

x = randint(1, 12)
y = randint(1, 12)

answer = x / y

your_answer = int(raw_input("What is %d / %d? " % (x, y)))

if answer == your_answer:
    print "Correct!"
else:
    print "Whoops, the answer is: %d" % answer
