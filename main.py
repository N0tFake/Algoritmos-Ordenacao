import os
from time import time

from numpy import outer
from Algoritmos.bubbleSort import bubbleSort
from Algoritmos.mergeSort import mergeSort
from Algoritmos.quickSort import quickSort
from Algoritmos.selectionSort import selectionSort
from Algoritmos.insertionSort import insertionSort
#from Algoritmos import bubbleSort, selectionSort
import inputFile


tamanho = 100
array = inputFile.getNumbers('aleatorio', tamanho)
array = [int(x) for x in array]

print("\033[92m"+ "\nO algoritmo está ordenando...\n" +" \033[0m")
 
start = time()
#output = bubbleSort(array)
#output = selectionSort(array)
#output = insertionSort(array)
#output = mergeSort(array)
output = quickSort(array)
end = time()

timeExec = end - start
timeExec = format(timeExec)

localPath = os.getcwd()
if not os.path.exists(localPath + '/Results/'):
    os.makedirs(localPath + '/Results/')

# output[0] = array ordenado
# output[1] = numero de comparações
# array[2] = numero de trocas
print(f'Resultados da ordenação de array com {tamanho} elementos')
print(f'\nTempo de execulção: {timeExec}')
print(f'\nNumero de comparações: {output[1]}')
print(f'\nNumero de Trocas: {output[2]}')
print(output[0])

#print('\n\n\nGerando arquivo com resultados . . .')

""" fileResut = open('./Results/' + str(tamanho) + '- random.txt', 'w')
fileResut.write(f'Resultados da ordenação de array com {tamanho} elementos')
fileResut.write(f'\nTempo de execulção: {timeExec}')
fileResut.write(f'\nNumero de comparações: {output[1]}')
fileResut.write(f'\nNumero de Trocas: {output[2]}')
fileResut.close()
 """