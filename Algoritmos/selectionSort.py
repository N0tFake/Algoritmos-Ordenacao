def selectionSort(array):
    trocas, comp = 0, 0
    for i in range(len(array)):
        menor = i
        for j in  range(i+1, len(array)):
            comp += 1
            if array[j] < array[menor]:
                menor = j
        
        if array[i] != array[menor]:
            temp = array[i]
            array[i] = array[menor]
            array[menor] = temp
            trocas += 1

    return [array, comp, trocas]