from random import randint

def trow(n):
#  ----- Retorna n tiros des dados
    #tiros = [randint(1, 6) for x in range(n)] Igual al ciclo for
    tiros =[]
    for _ in range(n): # genera n numeros random entre 1, 6   n = tiro de un dado
        tiros.append(randint(1, 6))
    
    return tiros

def count_dice(tiros):
# ------imprime los numeros de veces que salio cada cara
        #[print(f'{i} salio: {tiros.count(i)}') for i in range(1, 7)]   Igual al ciclo for
    for i in range(1, 7): # genera una lista de 1, 6 cada cara y cuenta cuantas veces salio ese numero
        print(f'{i} salio: {tiros.count(i)}')
    
    print(tiros)
