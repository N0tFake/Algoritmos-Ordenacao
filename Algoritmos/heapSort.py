def heapify(array, length, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < length and array[largest] < array[left]:
        largest = left

    if right < length and array[largest] < array[right]:
        largest = right
    
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, length, largest)

def heapSort(array):
    for i in range(len(array)//2 -1, -1, -1):
        heapify(array, len(array), i)
    
    for i in range(len(array)-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

    return [array, 0, 0]

    """ for i in range(len(array)-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i) """