def list(input):
    if (len(input) != 0):
        return (input[len(input)-1])
    else:
        return "Leere Liste"


liste = [1, 2, 3]
print(list(liste))
