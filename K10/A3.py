def selection(meineListe):
    sortedList = []
    lenght = len(meineListe)
    while (len(sortedList) != lenght):
        temp = meineListe[0]
        delete = 0
        for x in range(0, len(meineListe)):
            if (temp > meineListe[x]):
                temp = meineListe[x]
                delete = x
        sortedList.append(temp)
        meineListe.pop(delete)
    return sortedList


meineListe = [8, 4, 0, 2, 6, 5, 7, 1]
print(selection(meineListe))
