# https://platzi.com/comunidad/platzicodingchallenge-memory-parte-2-y-3/
from random import randint  #generar numeros aleatoreos
from os import system   # Para limpriar pantalle
from time import sleep  #Para esperar tiempo

def clear():  # este comando limpiara la pantalla
    clear = lambda: system('clear')
    return clear()


def get_code():  # Genera un codigo de 4 caranteres
    code ="#$%()/&"
    new_code = [code[randint(0,len(code)-1)] for _ in range(4)]
    return "".join(new_code)


def memory_game():
    code = get_code()  #L guarda el codigo generado
    input("Repite los caracteres en orden, Enter para continuar")
    clear()
    for i in code:
        print(i)   # imprime en pantalla cada caracter
        sleep(2)   # espera 2 segundos
        clear()    #Limpia pantalla

    repeat_code=input("Ingresa los caracteres en el orden en el que aparecieron: ")# Trata de repetir el codigo
    if repeat_code == code:  # si es igual ganaste, si no perdiste
        print("Ganaste --->",code)
    else:
        print("Perdiste")
        print("codigo correcto:",code)
        print("tu elejiste    :",repeat_code)


memory_game()

