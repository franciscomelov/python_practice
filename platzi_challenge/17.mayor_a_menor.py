# https://platzi.com/comunidad/platzicodingchallenge-ordenar-una-lista-de-numeros-de-mayor-a-menor/
from random import randint

def ordenar(numeros):
    print(numeros)
    ordenado = False # varieble que mientra no este ordenado el array sera falso
    while not ordenado:
        for i in range(len(numeros)-1): # ordenar
            if numeros[i] > numeros[i+1]: # si el numero a > b  se intercambian a y b van avanzando por el array
                numeros[i], numeros[i+1] = numeros[i+1], numeros[i]
                
        # CHECK
        for i in range(len(numeros)-1):
            if numeros[i] > numeros[i+1]:  # si detecta que a > b termina el ciclo de chequeo y vuelve a ordenas
                break
            elif i == len(numeros)-2:  # si a nunca fue mayor que b y llego al final del array, el array esta ordenado
                ordenado = True # unavez ordenado completamente ordenado == True
    print(numeros)


size = 100
numeros=[]
for _ in range(size):
    numeros.append(randint(-100,100))


ordenar(numeros)