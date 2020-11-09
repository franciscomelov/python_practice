def game_logic(user1, user2, counter_1, counter_2):
    if user1 == user2:
        print("Empate")

    else:
        if user1 == "piedra":
            if user2 == "tijera":
                print("Gana jugador 1")
                counter_1 += 1
            else:
                print("Gana jugador 2")
                counter_2 += 1
        elif user1 == "papel":
            if user2 == "piedra":
                print("Gana jugador 1")
                counter_1 += 1
            else:
                print("Gana jugador 2")
                counter_2 += 1
        elif user1 == "tijera":
            if user2 == "papel":
                print("Gana Jugador 1")
                counter_1 += 1
            else:
                print("Gana jugador 2")
                counter_2 += 1
        else:
            print("Gana jugador 2")
            counter_2 += 1
    return counter_1, counter_2


def game():
    counter_g = 0
    counter_1=0
    counter_2=0
    while counter_g <3:
        counter_g += 1
        
        user1 = input("Jugador 1: ")
        user2 = input("Jugador 2: ")
        counter_1, counter_2 = game_logic(user1, user2, counter_1, counter_2)
        print("")
    
    print("Jugador 1:",counter_1)
    print("Jugador 2:",counter_2)
    if counter_1 > counter_2:
        print("Gano jugador 1")
    elif counter_2 > counter_1:
        print("Gano jugador 2")
    else:
        print("Empate")

    




if __name__ == "__main__":
    game()

