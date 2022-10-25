
def selection(meineListe):
    finish = False
    count = len(meineListe)
    while (finish == False):
        finish = True
        temp = meineListe[0]
        delete = 0
        for x in range(0, count):
            if (temp > meineListe[x]):
                temp = meineListe[x]
                delete = x
                finish = False
        meineListe.append(temp)
        meineListe.pop(delete)
        count -= 1
    return meineListe


meineListe = [8, 4, 0, 2, 6, 5, 7, 1]
print(selection(meineListe))
