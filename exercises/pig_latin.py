# https://platzi.com/comunidad/platzicodingchallenge-traductor-de-_pig-latin_/

vowels = "aeiouAEIOUáéíóúÁÉÍÓÚ"  #diccionario de vocales
def convert(text):
    text = text.split()  # Separar por palabras en array
    latin =""
    
    for word in text:
        if word[0] in vowels:   # Si empieza en vocal
            latin += word +"way" + " "
        else:   #si em pieza en consonante
            latin += word[1:] + word[0] + "ay" + " "
    print(latin)

if __name__ == "__main__":
    #text = input("Introduce el texto: ")
    text = "onomatopeya"
    convert(text)