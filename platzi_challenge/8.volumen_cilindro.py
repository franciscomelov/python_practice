# https://platzi.com/comunidad/platzicodingchallenge-volumen-de-un-cilindro-numero-secreto/
from math import pi

def cilindro():
    r = float(input("Radio del cilindro: "))
    h = float(input("Altura del cilindro: "))
    vol = pi * (r**2) * h
    print(round(vol, 2))  #Redondeado a dos decimales


if __name__ == "__main__":
    cilindro()