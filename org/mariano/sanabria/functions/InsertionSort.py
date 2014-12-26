#Modulo InsertionSort.py
def insertSort(list):
    for i in range(1, len(list)):
        save = list[i]
        j = i
        while j > 0 and list[j - 1] > save:
            list[j] = list[j - 1]
            j -= 1
        list[j] = save
    return list
