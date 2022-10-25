import random

def bogoSort(array):
    def isSorted(array):
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                return False
        return True
    
    while not isSorted(array):
        random.shuffle(array)

    return [array, ' , ', ' ']