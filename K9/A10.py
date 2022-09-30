def questionAnswer():
    points = 0
    question = (input("Ich bin cool? (true or false)")).lower()
    print("Solution: true")
    if (question == "true"):
        points += 1
    question = (input("Python bin cool? (true or false)")).lower()
    print("Solution: false")
    if (question == "false"):
        points += 1
    question = (input("Java bin cool? (true or false)")).lower()
    print("Solution: true")
    if (question == "true"):
        points += 1
    print("DU hast", points, "Punkt/e erreicht")


questionAnswer()
