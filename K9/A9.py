from random import random

import random


def crackingNumber():
    inputUser = int(input("Eingabe:"))
    trys = 5
    win = False
    max = 100
    min = 0
    while (trys != 0):
        ran = random.randint(min, max)
        print(ran)
        if (inputUser == ran):
            print("The number is right. You are the winner Number:", ran)
            win = True
            break
        if (inputUser < ran):
            print("The Number is smaller")
            max = ran
        else:
            print("The Number is bigger")
            min = ran
        trys -= 1
    if (win == False):
        print("Loser. Number:", inputUser)


crackingNumber()
