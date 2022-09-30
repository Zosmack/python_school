def spritkosten():
    km = float(input("KM?: "))
    verbrauch = float(input("Verbrauch?: "))
    preisLiter = float(input("preisLiter?: "))
    return verbrauch/100*km*preisLiter
    # Verschleiß am Fahrzeug
    # Maut Gebühren


if __name__ == "__main__":
    print("H")
    # Die Funktionen werden nicht beim Import der Klasse ausgeführt
