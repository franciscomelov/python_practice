# https://platzi.com/comunidad/platzicodingchallenge-memory-part4-y-cuanto-vas-a-ahorrar-2/

def in_com(money):
    print(f'Cantidad inicial: {money}')


    for _ in range(6): money*=1.04  # seis meses
    print(f'en 6 meses generaste {money}')

    for _ in range(6): money*=1.04      # 12 meses
    print(f'en 1 año generaste {money}')
 
    for _ in range(12): money*=1.04  # 24 meses
    print(f'en 2 año generaste {money}')



money = 100   # Cantidad inicial

in_com(money)