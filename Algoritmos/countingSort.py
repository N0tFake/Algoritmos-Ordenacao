import numpy as np

def countingSort(array):
    comp, trocas = 0, 0

    max = np.max(array) + 1
    count = [0] * max

    for i in array:
        count[i] += 1
    
    for i in range(1, max):
        count[i] += count[i-1]
    
    outputArray =[0] * len(array)
    i = len(array) - 1
    while i >= 0:
        elem = array[i]
        count[elem] -= 1
        newPosition = count[elem]
        outputArray[newPosition] = elem
        comp += 1
        trocas += 1
        i -= 1
    
    return [outputArray, comp, trocas]