def wechselautomat(money):
    zwanzig = 0
    einer = 0
    while (money >= 20):
        if ((money-20) >= 0):
            zwanzig += 1
            money -= 20
    while (money != 0):
        einer += 1
        money -= 1
    print(zwanzig, "x 20€ Scheine und", einer, "x 1€ Münzen")


wechselautomat(55)
