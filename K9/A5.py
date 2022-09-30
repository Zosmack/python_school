def countingStars():
    inputUser = int(input("Stars?"))
    for x in range(1, inputUser+1):

        for y in range(1, x+1):
            # print(x)
            print("*", end='')

        print()


countingStars()
