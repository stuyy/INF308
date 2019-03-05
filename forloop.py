import random

counter = 0
randNum = 0

for x in range(10000000):
    randNum = random.randint(1, 500)
    if randNum == 500:
        print("It took " + str(counter) + " iterations to get the number 500.")
        break
    else:
        counter += 1
