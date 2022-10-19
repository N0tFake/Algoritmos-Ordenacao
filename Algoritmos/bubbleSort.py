def bubbleSort(array):
    trocas, comp = 0, 0
    for i in range(len(array)):
        comp += 1
        for j in range(len(array)-1, i, -1):
            comp += 1
            if array[j] < array[j-1]:
                aux = array[j]
                array[j] = array[j-1]
                array[j-1] = aux
                trocas += 1
    return [array, comp, trocas]