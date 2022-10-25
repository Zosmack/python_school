from hashlib import new


def blablub(lis, obj):
    if (lis.count(obj) <= 0):
        lis.append(obj)
    return lis


class Person:
    pass


p1 = Person()
lis = [p1]
print(blablub(lis, p1))
