# https://platzi.com/comunidad/platzicodingchallenge-puedo-ahorrar-otros-periodos-de-tiempo-puedo-ahorrar-en-otros-bancos/

def bank_1(money, años):
    años *=12
    print("---BANCO 1---")
    print(f'Cantidad inicial: {money}')
    for i in range(1, años+1):  # i es== a los meses
        money *= 1.04
        if i%12 ==0:  #Si i%12 es 0 sera un año y mostrara los ahorros
            print(f'en {i/12} años generaste: {money}')


def bank_2(money, años):
    años *=12
    print("---BANCO 2---")
    print(f'Cantidad inicial: {money}')
    for i in range(1, años +1):  # i es== a los meses
        money *= 1.03 #interes 3%
        if i%12==0: #Si i%12 es 0 sera un año y mostrara los ahorros
            money *= 1.07   # Si i%12 es==0   se cumplio un año  y se agrega un extra del 7%
            print(f'en {i/12} años generaste: {money}')






money = float(input("Ingresa la cantidad inicial: "))
años = int(input("Porcuantos años quieres hacer la comparacion: "))

bank_1(money, años)
bank_2(money, años)








