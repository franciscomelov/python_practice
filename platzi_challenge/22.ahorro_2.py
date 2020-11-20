# https://platzi.com/comunidad/platzicodingchallenge-que-pasaria-si/

def in_com(money):
    print(f'Cantidad inicial: {money}')
    

    for _ in range(6): money*=1.04
    print(f'en 6 meses generaste {money}')

    for _ in range(6): money*=1.04
    print(f'en 1 año generaste {money}')

    for _ in range(12): money*=1.04
    print(f'en 2 año generaste {money}')




money = float(input("Ingresa la cantidad inicial: "))


in_com(money)