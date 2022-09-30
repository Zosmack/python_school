def countingStars():
    inputUser = int(input("Stars?"))
    for x in range(1, inputUser+1):
        for y in range(1, x+1):
            print("*", end='')
        print()

    while (inputUser > 0):
        for x in range(1, inputUser):
            print("*", end='')
        inputUser -= 1
        print()


countingStars()
