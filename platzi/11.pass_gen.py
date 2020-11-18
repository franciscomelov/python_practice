#https://platzi.com/comunidad/platzicodingchallenge-generador-de-contrasenas/

from random import randint
diccionario= {   # diccionario con posibles tipos de caracteres
    "mayusculas" : "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ",
    "minusculas" : "abcdefghijklmnñopqrstuvwxyz",
    "caracteres" : "!#$%& ?¿¡/",
    "numeros" : "1234567890",
}



def generador(size, add):
    password =""
    while(len(password)< size):
        char = add[randint(0, len(add)-1)] # Del array add tomar demanera aleatoria una opcion de tipo de caracter
        password += diccionario[char][randint(0,len(diccionario[char])-1)]  # del diccionario se escoje una llave aleatoria guardada en char 
                                                                            # regresa el valor de la llave y se escoje otro numero aleatoreo
                                                                            #basado en el valor de lallave
    print(password)




if __name__ == "__main__":
    size = 8
    add = ["mayusculas", "numeros", "caracteres", "minusculas"]
    generador(size, add)
