##copy code into python consoleaa

import random

r = random.randint(1,100)
x = 101
while x !=r :
    x = int(input("Guess a number between 0 and 100. You can only exit, if you guess correctly! "))
    if x < r:
        print('higher')
    elif x > r:
        print('lower')
    else:
        print("correct, you guessed correctly!")
