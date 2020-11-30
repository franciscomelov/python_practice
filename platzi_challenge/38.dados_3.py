# https://platzi.com/comunidad/platzicodingchallenge-dia-38-juego-de-dados/
from random import randint

def game_dice():
    game_score={}  # diccionario para guadar jugador y tiros
    for player in range(1, 4):
        game_score[player] =[randint(1,6), randint(1,6) ] # secrea el jugador con el numero como key y 
                                                          #2 valores aleatoreos como value
    ganador="" # mensaje para ganador
    biggest_score = 0 #inicia el putje en cero
    for key, value in game_score.items(): # Itera sobre key value en el diccionario
        print(f'Jugador {key} : {value} = {sum(value)} ')  # Imprime key valuesum() suma el los numeros del array
        if sum(value) > biggest_score: # si el puntaje del jugador es mayor que biggest scores 
            biggest_score = sum(value) #biggest_score toma un nuevo puntaje mas alto, hasta completar iteracion
            ganador = f'EL ganador es: Jugador {key} con {sum(value)} puntos' 
            #Guarda en ganador mensaje copm puntaje y jugador


    print(ganador)


game_dice()

