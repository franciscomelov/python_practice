from os import system
def clear():
    clear = lambda: system('clear')
    return clear()

def make_board():
    board = []
    for i in range(5):
        board.append([])
        for v in range(5):
            board[i].append("x")
    for i in board:
        print(i)

def game():
    make_board()

    while True:
        salir = input("QUieres salir")
        if salir =="s":
            break
        clear() #Clean terminal
        make_board()


if __name__ == "__main__":
    game()


