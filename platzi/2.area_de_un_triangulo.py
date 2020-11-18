# isoceles 2 iguales, 1 diferente
# escaleno todos diferentes
# equilatero todos iguales
from math import sqrt

def triangulos(a, b, c):
    if a== b and b==c:
        print("equilatero")
        area = (a * (a/2 * sqrt(3) )) / 2
        print(area)
    elif a!=b and b!=c and c!=a:
        print("escaleno")
        pass
    else:
        print("isoceles")
        pass




if __name__ == "__main__":
    a = 22
    b = 22
    c = 22

    triangulos(a, b, c)
