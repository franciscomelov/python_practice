class Cards:
    def __init__(self, nombre, fuerza, defensa):
        self.nombre = nombre
        self.fuerza =fuerza
        self.defensa=defensa
    
    def card(self):
        print("----------")
        print("Nombre:",self.nombre)
        print("Fuerza:",self.fuerza)
        print("Defensa:",self.defensa)
        print("----------")

class Game:
    def __init__(self) :
        pass


#    Card(Nombre, fueza, defenza)
mago= Cards("Mago", 4, 2 )
sacerdotiza=Cards("Sacerdotiza", 1, 5)
emperatriz=Cards("Emperatriz",3, 2 )
emperador=Cards("Emperador", 2, 3)
enamorado=Cards("Enamorado", 4, 1)

mago.card()
emperatriz.card()

