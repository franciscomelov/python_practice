#  https://platzi.com/comunidad/platzicodingchallenge-te-conviene-esta-apuesta/

from random import randint


def gess():
    numero = randint(1, 100)
    
    dinero = 4  #Empiezas en cuatro dolares
    print("------",numero)
    # high - low son los valores minimos y maximos
    high =100
    low = 1
    gess = int(high/2) # opcion dada siempre sera la mitad entre low - high
    while True: #ciclo par adivinar
        print(low, high)
        print("numero es? :", gess) # imprime gess
        
        if gess== numero: # si gess == numero  termina el ciclo
           print("GANE tu numero es:", numero)  
           break
        
        if gess > numero:  # si gess>numero se toma la mitad baja  de gess hacia low
            print("_____________________")
            print("MAS BAJO")
            high = gess -1  # si gess gue 50  high toma 49 porque 50 ya sabemos que no es
            gess = high - int( round(high - low) /2)  # gess es la mitad de high    1-----10  -> guess==5 10/2
        else: # guess < numero se toma la mitad alta de guess hacia high
            print("_____________________")
            print("MAS ALTO")
            low = gess +1 
            gess = high - int( round(high - low) /2)  #   high es el mismo asi que podemos solo dividir high/2
                                                          #se hace otra operacion  (high-low) / 2

        dinero -=1  # se resta dinero 

    
    print("dinero",dinero)


print("Quieres jugar")
gess()

