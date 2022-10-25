def password(passwords):
    solution = []
    for x in passwords:
        contains = x.count("ab")
        contains += x.count("ba")
        if (contains != 0):
            solution.append(x)
    return solution


passwords = ["ababa", "baab", "sdiopc", "ajkwei", "bab"]
print(password(passwords))
