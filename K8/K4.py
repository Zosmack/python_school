
def phone(price, camera, charge, marke):
    if (price < 1000 and camera >= 3 and charge >= 2 and marke.lower() == ("apple" or " samsung")):
        print("kaufen")
    else:
        print("nicht kaufen")


phone(999, 12, 2, "Apple")
