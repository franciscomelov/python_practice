# https://platzi.com/comunidad/platzicodingchallenge-31-teorema-de-pitagoras/

def teorema(punto_a,punto_b):
    a = abs(punto_a[0] - punto_b[0])  # valor en x
    b= abs(punto_a[1] - punto_b[1])   # valor en y
    #Nopuede haber una distanciaen negativo abs() regresa el valor avsoluto
    #Ya se puede ocupar la formula
    c = (a**2 + b**2)**(1/2)   #elevar a 1/2  es igual que sacar la raiz cuadrada
    print(c)


punto_a = [3, 4]  # no escribo a porque es el punto en la grafica
punto_b = [5, 7]  # para no confundirse con  el a de la formula
teorema(punto_a, punto_b)

""" 

Punto A = (3, 4) # lugar en 
Punto B = (5, 7) # grafica
Distancia = 3.605551

En X el espacio en entre 3 y 5 = 2 
a=2
en Y el espacio entre 7 y 4 es = 3
b = 3
Ya se puede ocupae 
a**2  +  b**2  =  c**2

            |
            |         0 (5, 7)
            |         |  
            |         |  
            |     0___|  
            |  (3,4)       
            |               
            |               
____________|______________
            |
            |
            |
            |
            |
            |
"""