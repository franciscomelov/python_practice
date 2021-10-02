# https://platzi.com/clases/2255-python-intermedio/36475-reto-final-juego-del-ahorcado-o-hangman-game/
from os import system
from random import randint
import random
import time

def welcome():
    saludo = "Bienvenido \n Al juego \ndel Ahorcado" 
    for i, _ in enumerate(saludo):
        system("clear")
        print(saludo[:i+1])
        time.sleep(.1)
    time.sleep(.4)


def doll():
    HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']
    return HANGMANPICS


def get_data():
    with open("./data.txt", "r", encoding="utf-8") as f:
        words = {i:word[:-1] for i,word in enumerate(f)}
    return words


def get_word():
    # random_index = words.get([randint(0, len(words)-1)])
    words = get_data()
    word = random.choice(words)
    hidden_word = len(word)*"_".split()
    #print(word)
    return word, hidden_word

def check_errors(word):
    try:
        if len(word) ==0:
            raise ValueError("!!Escribe algo¡¡")
        elif not word.isalpha():
            raise ValueError("Solo ingresa palabras")
        return False
    except Exception as e:
        print(e)
        return True


def run():
    word, hidden_word = get_word()
    playing = True
    counter = 0
    HANGMANPICS = doll()
    
    while playing:
        system("clear")
        print(HANGMANPICS[counter])
        print(" ".join(hidden_word))

        print("word:",word)
        print("hidden_word:",hidden_word)
        gess_letter = input("Adivina la la palabra: ")

        if check_errors(gess_letter): counter-=1



        
        if word.__contains__(gess_letter) and  hidden_word.__contains__(gess_letter):
            for i, hidden  in enumerate(word):
                if gess_letter == hidden:
                    hidden_word[i] = gess_letter
        else:
            counter+=1
            
        
        
        if "_" not in hidden_word:
            print("G A N A S T E")
            print(f'Tenminaste en {counter} turnos')
            print("¡¡¡F I N !!!")
            break
        elif counter==len(HANGMANPICS):
            print("P E R D I S T E")
            print(f"La palabra es: {word}")
            break



if __name__ == "__main__":
    #welcome()
    run()


