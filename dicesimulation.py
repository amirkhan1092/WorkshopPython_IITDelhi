from random import randint
max = 6
min = 1
while 1:
    if not input('for next roll please enter and another key for exit  '):

        print(randint(min, max))
    else:
        break