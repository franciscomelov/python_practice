from random import randint


def vacas_toros():
    while True: #loop hasta obtener 4 numeros diferentes
        xxxx = str(randint(1000,9999))
        if  len(set(xxxx)) ==4:
            break

    print(xxxx )
    
    
    
    vacas = 0
    toros = 0

    while vacas<10:


        vacas_temp=0
        toros_temp=0
        number = input("Escribe un numero de cuatro digitos: ")
        
        for digit in set(number): #comparar cada numero de number en xxxx en set() para quitar numeros repetifos
            if digit in xxxx:
                vacas_temp += 1
            else:
                toros_temp +=1

        if vacas_temp == 4: #si coinciden todos los numeros
            print("numero correcto")
            break
        

        print(f'Tuviste:  {vacas_temp} vacas')
        print(f'Tuviste {toros_temp} toros')
        print("________________________________")

        toros += toros_temp
        vacas += vacas_temp

    print(f'{vacas} vacas totales')
    print(f'{toros} toros totales')




vacas_toros()