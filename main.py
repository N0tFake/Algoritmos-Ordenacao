import os
from time import sleep, time

from Algoritmos.bogoSort import bogoSort
from Algoritmos.bubbleSort import bubbleSort
from Algoritmos.countingSort import countingSort
from Algoritmos.mergeSort import mergeSort
from Algoritmos.quickSort import quickSort
from Algoritmos.selectionSort import selectionSort
from Algoritmos.insertionSort import insertionSort

import inputFile

tamanho = 1000000
ordem = 'aleatorio'
array = inputFile.getNumbers(ordem, tamanho)
array = [int(x) for x in array]

print("\033[92m"+ "\nO algoritmo está ordenando...\n" +" \033[0m")
 
start = time()
#output = bubbleSort(array)
#output = selectionSort(array)
#output = insertionSort(array)
#output = mergeSort(array)
#output = quickSort(array)
#output = bogoSort(array)
#output = countingSort(array)
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
print(f'Os elementos estavam em ordem: {ordem}')
print(f'\nTempo de execulção: {timeExec} segundos')
print(f'\nNumero de comparações: {output[1]}')
print(f'\nNumero de Trocas: {output[2]}')
#print(output[0])

#print('\n\n\nGerando arquivo com resultados . . .')

""" fileResut = open('./Results/' + str(tamanho) + '- random.txt', 'w')
fileResut.write(f'Resultados da ordenação de array com {tamanho} elementos')
fileResut.write(f'\nTempo de execulção: {timeExec}')
fileResut.write(f'\nNumero de comparações: {output[1]}')
fileResut.write(f'\nNumero de Trocas: {output[2]}')
fileResut.close()
 """