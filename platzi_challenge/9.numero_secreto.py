# https://platzi.com/comunidad/platzicodingchallenge-volumen-de-un-cilindro-numero-secreto/
from random import randint 


def guess(n):
    counter =0
    while True:
        counter +=1
        user = int(input("Adivina el numero: "))
        print("")

        if user == n:
            print(f"Adivinate el numero en {counter} intentos")
            break
        elif user >n:
            print("El numero es menor")
        else:
            print("El numero es mayor")


if __name__ == "__main__":
    higher  = int(input("Del 1 a que numero quieres adivinar: ")) 
    n = randint(1, higher)
    guess(n)