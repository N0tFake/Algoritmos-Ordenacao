def particion(array, init, end):
    trocas, comp = 0, 0
    pivo = array[end-1]
    for i in range(init, end):
        comp += 1
        if array[i] > pivo:
            end +=1
        else:
            end += 1
            init += 1
            array[i], array[init - 1] = array[init - 1], array[i]
            trocas += 1

    return [init - 1, comp, trocas]

def quickSort(array, init = 0, end=None):
    trocas, comp = 0, 0
    end = end if end is not None else len(array)
    if init < end:
        output = particion(array, init, end)
        part = output[0]
        comp += output[1]
        trocas += output[2]
        quickSort(array, init, part)
        quickSort(array, part+1, end)

    return [array, comp, trocas] 
