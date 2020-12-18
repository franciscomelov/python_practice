from random import choice, randint

def robot(mov, max):
           # x y
    punto = [0,0]

    counter =0
    while counter < mov:
        counter += 1
        direccion = choice(["arriba", "abajo", "izquierda", "derecha"])
        pasos = randint(0, max)

        if direccion== "arriba":    punto[1] += pasos
        elif direccion== "abajo":   punto[1] -= pasos
        elif direccion== "izquierda":   punto[0] -= pasos
        elif direccion== "derecha":    punto[0] += pasos



        print("Direccion: ", direccion)
        print("Pasos:  ",pasos)
    
    print("Punto final: ", punto)



mov = 5 # cantidad ovimientos a los laod
max= 5 # maximo de pasos
robot(mov, max)

