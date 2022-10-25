from re import T


def wechselautomat(money):
    fünfizig = 0
    zwanzig = 0
    zehner = 0
    fünfer = 0
    zweier = 0
    einer = 0
    while (money >= 50):
        fünfizig += 1
        money -= 50
    while (money >= 20):
        zwanzig += 1
        money -= 20
    while (money >= 10):
        zehner += 1
        money -= 10
    while (money >= 5):
        fünfer += 1
        money -= 5
    while (money >= 2):
        zweier += 1
        money -= 2
    while (money != 0):
        einer += 1
        money -= 1
    print(fünfizig, "x 50€", zwanzig, "x 20€", zehner, "x 10€",
          fünfer, "x 5€", zweier, "x 2€", einer, "x 1€ Münzen")


def wechselautomattwo(money):
    if (money >= 50):
        temp = 0
        while (money >= 50):
            temp += 1
            money -= 50
        print(temp, "x 50€", end=" ")
    if (money >= 20):
        temp = 0
        while (money >= 20):
            temp += 1
            money -= 20
        print(temp, "x 20€", end=" ")
    if (money >= 10):
        temp = 0
        while (money >= 10):
            temp += 1
            money -= 10
        print(temp, "x 10€", end=" ")
    if (money >= 5):
        temp = 0
        while (money >= 5):
            temp += 1
            money -= 5
        print(temp, "x 5€", end=" ")
    if (money >= 2):
        temp = 0
        while (money >= 2):
            temp += 1
            money -= 2
        print(temp, "x 2€", end=" ")
    if (money != 0):
        temp = 0
        while (money >= 1):
            temp += 1
            money -= 1
        print(temp, "x 1€")


wechselautomat(55)
wechselautomattwo(55)
