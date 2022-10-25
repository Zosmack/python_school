def meinSort(meineListe):
    finish = False
    while (finish == False):
        finish = True
        for x in range(0, len(meineListe)-1):
            if (meineListe[x] > meineListe[x+1]):
                meineListe[x], meineListe[x+1] = meineListe[x+1], meineListe[x]
                finish = False
    return meineListe


meineListe = [8, 4, 0, 2, 6, 5, 7, 1]
print(meinSort(meineListe))
