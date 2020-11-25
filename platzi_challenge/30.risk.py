# https://platzi.com/comunidad/platzicodingchallenge-dia-30-risk-3/

from random import randint
def game():
    # Se crean 2 array atacabte y defensor
    atacante = sorted([randint(1,7) for x in range(3)], reverse=True)
    defensor = sorted([randint(1,7) for x in range(2)], reverse=True)
    # in ciclo for para cada jugador dentro de un sorted   reverse=Ture  permite 
    #acomodar de mayor a menor

    # Se imprimen los dos jugadores
    print("Atacante:",atacante)
    print("Defensor:",defensor)
#Ciclo for valor 2 porque solo se hacen 2 comparaione del defensor
    for i in range(2):# comparan los valores primero [0]  y despues [1]
        if atacante[i] > defensor[i]:  # Sigana el atacante
            diferencia = atacante[i] -defensor[i]
            print(f"Defensor pierde: {diferencia} ({atacante[i]} es mayor que {defensor[i]})")
        elif defensor[i] > atacante[i]: # Si gana el defensor
            diferencia = defensor[i] -atacante[i]
            print(f"Atacante pierde: {diferencia} ({defensor[i]} es mayor que {atacante[i]})")
        else: #Si empatan
            print(f"Empate: ({defensor[i]} y {atacante[i]} son iguales)")

if __name__ == "__main__":
    game()
