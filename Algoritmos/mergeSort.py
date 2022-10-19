from numpy import arange


def mergeSort(array):
    trocas, comp = 0, 0
    if len(array) > 1:
        mid = len(array)//2

        arrayLeft = array[:mid]
        arrayRight = array[mid:]

        mergeSort(arrayLeft)
        mergeSort(arrayRight)
    
        i, j, k = 0, 0, 0

        while i < len(arrayLeft) and j < len(arrayRight):
            if arrayLeft[i] < arrayRight[j]:
                array[k] = arrayLeft[i]
                i += 1
            else:
                array[k] = arrayRight[j]
                j += 1
            k += 1
            comp += 1
            trocas += 1
        
        while i < len(arrayLeft):
            array[k] = arrayLeft[i]
            i += 1
            k += 1

            comp += 1
            trocas += 1
        
        while j < len(arrayRight):
            array[k] = arrayRight[j]
            j += 1
            k += 1

            comp += 1
            trocas += 1
        
        return [array, comp-1, trocas]