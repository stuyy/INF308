# Anson Foong, INF 308
# This program is a simulation of the popular Magic 8-ball.

import random

def generateNumber():
    return random.randint(1, 10)

print("Hoo-rah! You've activated UAlbany's Magic 8-ball. Think of a yes or no question!")
question = input()
print("Now press any key and the power of the almighty Danes will get together and determine your faith.")
key = input()
randomNumber = generateNumber()

if randomNumber == 1:
    print("From what I can see with my own Magic 8-Ball, I would say the chances are in your favor :)")
elif randomNumber == 2:
    print("I definitely see it happening for you")
elif randomNumber == 3:
    print("There's no doubt about it.")
elif randomNumber == 4:
    print("Indeed you will.")
elif randomNumber == 5:
    print("Maybe ask again later, I'm busy helping other clients.")
elif randomNumber == 6:
    print("Why don't you ask a better question?")
elif randomNumber == 7:
    print("I'm the wrong person to ask that question pal.")
elif randomNumber == 8:
    print("You're doomed if you're counting on it.")
elif randomNumber == 9:
    print("I would not get my hopes up.")
elif randomNumber == 10:
    print("From the looks of my Magic 8-ball, it says no.")