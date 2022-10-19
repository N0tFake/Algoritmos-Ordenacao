def getNumbers(type, tamanho):
    if type == 'ordenado':
        with open('./files/'+str(tamanho)+'/'+str(tamanho)+' - Ordenado.txt', 'r') as file:
            return file.readline().split(' ')
        ...
    elif type == 'decrecente':
        with open('./files/'+str(tamanho)+'/'+str(tamanho)+' - Decrescente.txt', 'r') as file:
            return file.readline().split(' ')
        ...
    elif type == 'aleatorio':
        with open('./files/'+str(tamanho)+'/'+str(tamanho)+' - Aleatorio.txt', 'r') as file:
            return file.readline().split(' ')
        ...
    else:
        return ['error']
