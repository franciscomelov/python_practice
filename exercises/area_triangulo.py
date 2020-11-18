#  isósceles = 2 lados iguales
#  equilátero = tres lado iguales
#  escaleno = diferente
from math import sqrt

def triangulo(a, b , c):
    if a == b and b ==c: 
        print("Tu triangulo es:  equilátero")
        area = (sqrt(3) / 4) * (a ** 2 )
        print(f"Su area es = {area}")

    elif a != b and b != c and  a!=c:
        print("Tu triangulo es: escaleno")
        s = (a+b+c) / 2.0
        area = sqrt(s*(s-a)*(s-b)*(s-c))
        print(area)
    else:
        print("Tu triangulo es: isósceles")
        if [a,b,c].count(a) == 1:
            base = a
            a = b
        elif [a,b,c].count(b) == 1:
            base = b
        else:
            base = c
        area = (base * (sqrt(a**2 -(base**2 / 4)))) /2
        print(area)


if __name__ == "__main__":
    print("Ingresa los 2 lados de u triangulo")
    a = int(input("Primer lado: "))
    b = int(input("Segundo lado: "))
    c = int(input("Tercer lado: "))
    triangulo(a, b, c)


"""


   /\
  /  \
 /    \
/      \
--------

"""