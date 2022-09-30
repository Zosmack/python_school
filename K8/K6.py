def game(ein):
    match ein:
        case "Stein":
            print(ein)
        case "Schere":
            print(ein)
        case "Papier":
            print(ein)
        case _:
            print("Weder noch")


def gameSwitch(ein):
    list = {
        1: "Stein",
        2: "Schere",
        3: "Papier"
    }
    print(list.get(ein, "invalid"))


gameSwitch(1)
game("Stein")
