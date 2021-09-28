# https://platzi.com/clases/2255-python-intermedio/36475-reto-final-juego-del-ahorcado-o-hangman-game/
from random import randint
from typing import Counter

def get_data():
    with open("./data.txt", "r", encoding="utf-8") as f:
        words = {i:word[:-1] for i,word in enumerate(f)}
    return words


def get_word():
    word = words[randint(0, len(words)-1)]
    hidden_word = len(word)*"_".split()
    print(word)
    return word, hidden_word


def run():
    word, hidden_word = get_word()

    playing = True
    counter = 0
    while playing:

        print(" ".join(hidden_word))
        gess_letter = input("Adivina la la palabra: ")

        if gess_letter in word:
            for i, hidden  in enumerate(word):
                if gess_letter == hidden:
                    hidden_word[i] = gess_letter

        if "_" not in hidden_word: break
        counter+=1

    print(f'Tenminaste en {counter} turnos')
    print("¡¡¡F I N !!!")


if __name__ == "__main__":
    words = get_data()
    run()

