""" 
EL mago: magia
    ataque: echizo
    fueza: 5
    resistencia:2

Sacerdotiza: proteccion
    efectp:proteccion-aumenta*.5 resistencia de una carta atacada
    fuerza:1
    resistencia: 5

: aumenta fuerza de otra carta
    efecto: aumento de fuerza *.3 a otra carta
    fuerza:Emperatriz
    resistencia:

Emperador: quita fuerza a otra carta
    ataque:  golpe
    fuerza:2
    resistencia:3

El enamorado: roba una carta
    ataque: golpe limpio
    fuerza: 4
    resistencia:2

Ataque:
resistencia 10-100
Fuerza, 1-50
 """

class Card:
    def __init__(self, nombre, fuerza, defensa):
        self.nombre = nombre
        self.fuerza =fuerza
        self.defensa=defensa



#    Card(Nombre, fueza, defenza)
mago= Card("Mago", 4, 2 )
sacerdotiza=Card("Sacerdotiza", 1, 5)
emperatriz=Card("Emperatriz",3, 2 )
emperador=Card("Emperador", 2, 3)
enamorado=Card("Enamorado", 4, 1)
print(mago)
