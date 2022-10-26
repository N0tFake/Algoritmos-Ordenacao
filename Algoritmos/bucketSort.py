from Algoritmos.insertionSort import insertionSort

def bucketSort(array):
    comp, trocas = 0, 0

    maxValue = max(array)
    size = maxValue/len(array)

    bucketList = [[] for i in range(len(array))] 
    
    for i in range(len(array)):
        j = int(array[i]/size)
        comp += 1
        if j != len(array):
            bucketList[j].append(array[i])
        else:
            bucketList[len(array)-1].append(array[i])

    for i in range(len(array)):
        output = insertionSort(bucketList[i])
        bucketList[i] = output[0]
        comp += output[1]
        trocas += output[2]
    
    outputArray = []
    for i in range(len(array)):
        outputArray = outputArray + bucketList[i]
   
    return [outputArray, comp, trocas]