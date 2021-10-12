from os import system
#import keyboard


def clear():
    clear = lambda: system('clear')
    return clear()

def make_board(x,y):
    if x > 4: x = 4
    if y > 4: y = 4
    if x < 0: x = 0
    if y < 0: y = 0

    board = []
    for i in range(5):
        board.append([])
        for v in range(5):
            board[i].append("#")
    
    board[x][y] = "X"
    
    for i in board:
        print(i)
    return x, y

def game():
    x, y = 0, 0
    make_board(x,y)

    while True:
        print("presiona [a, w, s, d] para moverte  [salir] para salir")
        move = input(" ")

        if move =="salir": break
        elif move == "a": y -= 1 #Izquierda
        elif move == "w": x -=1  #Arriba
        elif move == "s": x += 1 #Abajo
        elif move == "d": y += 1 #Derecha





        clear() #Clean terminal
        x,y =make_board(x,y)


if __name__ == "__main__":
    game()


