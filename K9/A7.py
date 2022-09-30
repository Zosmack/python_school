from random import random


import random


def crackingNumber():
    ran = random.randint(0, 100)
    trys = 5
    win = False
    while (trys != 0):
        inputUser = int(input("Eingabe:"))
        if (inputUser == ran):
            print("The number is right. You are the winner Number:", ran)
            win = True
            break
        if (inputUser < ran):
            print("The Number is bigger")
        else:
            print("The Number is smaller")
        trys -= 1
    if (win == False):
        print("Loser. Number:", ran)


crackingNumber()
