# https://platzi.com/comunidad/platzicodingchallenge-dia-28-codigo-morse-y-29-telefono/

phone ={
2:"ABC",
3:"DEF",
4:"GHI",
5:"JKL",
6:"MNO",
7:"PRS",
8:"TUV",
9:"WXY"
}

def conbinations(phone, phone_number):
    letters =[]  # Array donde se guardaran las comnibacinoes
    #Inica guardando en letters las letras que represantan cada numero del arrai
    for x in phone_number:  # ciclo que itera por cada numero del array phone number
        letters.append(phone[x])   #  hace append al array letters los valores que representa cada numero del array phone number
    print(letters)
    #['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PRS', 'TUV']
    while(True): # inicia ciclo while
        temp = []  # array temporal para guardar conbinaciones
 
         # El ciclo ira conbinando de grupos de dos  letters[0]   letters[1]
        for i in letters[0]:     # Itera porcada valor de letters[0]
            for j in letters[1]: #Itera por cada valor de letters[1]
                temp.append(i + j)  #Hace append a array temp i + j  seran cada combinacion posibles entre 2 grupos letters[0] y letters[1]
        # Cada  combinacion posible entre 2 grupos se guardo en temp
        letters[0] = temp # Letters[0] ahora temp
        del letters[1] # eliminamos letter[1]
        #Letters[0] es cada combinacion entre los dos primeros grupos
        #letter[1] ahora es un nuevo gripo a conbinar


        if len(letters) == 1: # cuando el tama ñano de letters sea uno ya no hay mas grupos para conbinar y sale del ciclo
            break
    #print(letters)
    print(len(letters[0]))  #imprime cuantas conibnaciones fueron posibles







# phone = diccionario con alfabeto teclado
# el array es la combinacion de numeros
conbinations(phone,[2,3,2,5,6,7, 8])

# el resultado es  3 * 3 * 3 * 3 * 3 * 3 * 3 = 2187
# 3 = caracteres disponibles a conbinar
# se multiplica 7 veces  = el largo de la combinacion

"""
#1  Ejemplo con tres dijitos
    ABC   DEF   GHI

primera conbinacions
ABC
A
B
C

SEGUNDA COMBINACION  ENTRE PRIMER GRUPO Y SEGUNDP
ABC  DEF
a d
a e
a f
b d
b e
b f
c d
c e
c f

TERCERA COMBINACION
[a d
a e
a f
b d
b e
b f
c d
c e
c f]  => este es el primer grupo ahora  el segundo grupo es GHI

asi ira iterando hasta pasar por los 7 digitos que es el tamaños de nuestra combinacion


"""