from math import pi
def volumen(r, h):
    vol = pi * (r**2) * h
    print(round(vol, 2))

if __name__ == "__main__":
    #r = float(input("Radio del cilindro: "))
    #h = float(input("Altura del cilindro"))
    r = 5
    h = 6
    volumen(r,h)
