import random


def kino():
    loge = [["[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]"],
            ["[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]"]]

    room = [["[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]"],
            ["[  ]", "[  ]", "[  ]", "[  ]", "[  ]",
                "[  ]", "[  ]", "[  ]", "[  ]"],
            ["[  ]", "[  ]", "[  ]", "[  ]", "[  ]",
                "[  ]", "[  ]", "[  ]", "[  ]"],
            ["[  ]", "[  ]", "[  ]", "[  ]", "[  ]",
                "[  ]", "[  ]", "[  ]", "[  ]"],
            ["[  ]", "[  ]", "[  ]", "[  ]", "[  ]",
                "[  ]", "[  ]", "[  ]", "[  ]"],
            ["[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]"]]
    setSeats(room)
    setSeats(loge)
    printArray(room)
    printArray(loge)


def setSeats(array):
    numberSeatSeats = int((8*len(array))/3)
    while (numberSeatSeats > 0):
        one = random.randint(0, len(array)-1)
        two = random.randint(0, 8)
        array[one][two] = "[OO]"
        numberSeatSeats -= 1


def printArray(array):
    for x in range(len(array)):
        print(array[x])
    print()


kino()
