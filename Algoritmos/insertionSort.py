def insertionSort(array):
    trocas, comp = 0, 0
    for i in range(len(array)):
        key = array[i]
        j = i
        comp += 1
        while j > 0 and key < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
            trocas += 1

        array[j] = key
    
    return [array, comp-1, trocas]