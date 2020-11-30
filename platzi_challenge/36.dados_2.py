# https://platzi.com/comunidad/platzicodingchallenge-numeros-aleatorios-2/

from random import randint

def tirar_dados(n, caras):
    tiros =[]
    #tiros = [randint(1, caras) for x in range(n)]   Igual al ciclo for
    for _ in range(n): # genera n numeros random entre 1, 6   n = tiro de un dado
        tiros.append(randint(1, caras)) # caras se usa como segundo parametro de re¿andint
                                        # si caras=10  habra valores de 1 al 10  
    
    ##[print(f'{i} salio: {tiros.count(i)}') for i in range(1, 7)]   Igual al ciclo for
    for i in range(1, 7): # genera una lista de 1, 6 cada cara y cuenta cuantas veces salio ese numero
        print(f'{i} salio: {tiros.count(i)}')

    print(tiros)

#El codigo es igual al anterios
#solo se añade la variable caras
n=10
caras = 16  # 
tirar_dados(n, caras)