import os




def players():
    player_1 = input("Escribe tu nombre: ")
    player_2 = input("Escribe tu nombre: ")
    return player_1, player_2

def show_board(board):
    for row in board:
        print(*row, sep="|")

def turn(board, idx, mark):
    if idx in[1,2,3]:
        board[0][idx-1] = mark
    elif idx in [4, 5, 6]:
        board[1][idx-4] = mark
    elif idx in [7, 8, 9]:
        board[2][idx-7] = mark
    return board

def check_win(board, mark):
    if mark == board[0][0]== board[0][1] == board[0][2]:
        return True
    if mark == board[1][0]== board[1][1] == board[1][2]:
        return True
    if mark == board[2][0]== board[2][1] == board[2][2]:
        return True

    if mark == board[0][0]== board[1][0] == board[2][0]:
        return True
    if mark == board[0][1]== board[1][1] == board[2][1]:
        return True
    if mark == board[0][2]== board[1][2] == board[2][2]:
        return True

    if mark == board[0][0]== board[1][1] == board[2][2]:
        return True
    if mark == board[0][2]== board[1][1] == board[2][0]:
        return True
    
    return False

def new_board():
    return [["1", "2", "3",], 
             ["4", "5", "6",],
             ["7", "8", "9",] ]

def main():
    player_1, player_2 = players()
    score = {"score_1":0, "score_2": 0}

    playing = True
    board = new_board()
    counter_1= 0 
    counter_2 = 0

    while playing:
        os.system("cls")
        print(f"Turno de {player_1}")
        show_board(board)
        idx =input("Elige un espacio para tirar: ")
        if idx == "salir": break
        board = turn(board, int(idx), "X")
        if check_win(board, "X"):
            print(f"Gano {player_1}")
            counter_1 +=1
            input("enter para continuar")
            board = new_board()
        
        

        os.system("cls")
        print(f"Turno de {player_2}")
        show_board(board)
        idx =input("Elige un espacio para tirar: ")
        if idx == "salir": break
        board = turn(board, int(idx), "O")
        if check_win(board, "O"):
            print(f"Gano {player_1}")
            counter_2 +=1
            input("enter para continuar")
            board = new_board()
        # os.system("cls")
    
    print(f"{player_1} gano: {counter_1}")
    print(f"{player_2} gano: {counter_2}")


        




if __name__ == "__main__":
    main()