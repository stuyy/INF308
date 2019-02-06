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
    print("")
