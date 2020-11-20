# https://platzi.com/comunidad/platzicodingchallenge-puedo-ahorrar-otros-periodos-de-tiempo-puedo-ahorrar-en-otros-bancos/

def in_com(money, meses):
    print(f'Cantidad inicial: {money}')
    

    for i in range(1, meses[len(meses)-1]+1):  # i es== a los meses
        money *= 1.04
        if i in meses:  #i los meses transcurridos esta en meses lista a mostrar mostra ra la cantidad
            print(f'en {i} meses generaste: {money}')






money = float(input("Ingresa la cantidad inicial: "))
meses = input("Ingresa los meses que quieres ver separados por coma: ").split(",")
meses = [int(mes) for mes in meses]

in_com(money, meses)