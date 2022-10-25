def quicksort(unSort):
    if (len(unSort) == 1):
        return unSort
    unSortBigger = []
    pivot = unSort.pop(len(unSort)-1)
    change = 0
    for count in range(0, len(unSort)+change):
        if (unSort[count-change] > pivot):
            unSortBigger.append(unSort[count-change])
            unSort.pop(count-change)
            change += 1
    if (len(unSortBigger) == 1 or len(unSortBigger) == 0):
        unSortBigger.append(pivot)
        pivot = "False"
    else:
        unSortBigger = quicksort(unSortBigger)
    if (pivot != "False"):
        unSort.append(pivot)
    if (len(unSort) != 1):
        if (len(unSort) != 0):
            unSort = quicksort(unSort)
    return unSort+unSortBigger


meineListe = [8, 4,  9, 7, 1, 2, 5, 3, 0, 3]
print(quicksort(meineListe))
