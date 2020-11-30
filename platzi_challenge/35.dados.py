# https://platzi.com/comunidad/platzicodingchallenge-numeros-aleatorios/
from random import randint

def tirar_dados(n):
    #tiros = [randint(1, 6) for x in range(n)] Igual al ciclo for
    tiros =[]
    for _ in range(n): # genera n numeros random entre 1, 6   n = tiro de un dado
        tiros.append(randint(1, 6))
    
    #[print(f'{i} salio: {tiros.count(i)}') for i in range(1, 7)]   Igual al ciclo for
    for i in range(1, 7): # genera una lista de 1, 6 cada cara y cuenta cuantas veces salio ese numero
        print(f'{i} salio: {tiros.count(i)}')

    print(tiros)

n=10
tirar_dados(n)