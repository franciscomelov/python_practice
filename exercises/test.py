import math
def run(simbol, lines):
    if lines%2 == 0:
        lines +=1
    half = math.floor(lines/2)

    for line in range(1,half+1):
        print(simbol * line)

    for line in range(half+1,0,-1):
        print(simbol * line)


if __name__ == "__main__":
    simbol = input("Que simbolo quieres usar: ")
    lines = int(input("Cuantos saltos de linea quieres(numero impar): "))
    run(simbol, lines)


"""
Mostrar en pantalla 
#####
####
###
##
#
"""