from math import pi

def cilindro():
    r = float(input("Radio del cilindro: "))
    h = float(input("Altura del cilindro"))
    vol = pi * (r**2) * h
    print(round(vol, 2))

def esfera():
    radio = float(input("Ingresa el radio de la esfera: "))
    volumen = (4 * pi * radio**3)/3
    print(volumen)

def cubo():
    lado = float(input("Engresa el tamaños de un lado del cubo: "))
    volumen = lado **3
    print(volumen)

if __name__ == "__main__":
    print("Elije la figura que quieres calcular volumen, (1, 2, ó 3)")
    opcion = input("""
1 - cilindro
2 - esfera
3 - cubo
 """)
    while True:
        if opcion == "1":
            cilindro()
            break
        elif opcion =="2":
            esfera()
            break
        elif opcion == "3":
            cubo()
            break
        else:
            print("Opcion incorrecta")