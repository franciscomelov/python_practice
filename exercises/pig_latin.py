vowels = "aeiouAEIOUáéíóúÁÉÍÓÚ"
def convert(text):
    text = text.split()
    latin =""
    
    for word in text:
        if word[0] in vowels:
            latin += word +"cay" + " "
        else:
            latin += word[1:] + word[0] + "ay" + " "
    print(latin)

if __name__ == "__main__":
    #text = input("Introduce el texto: ")
    text = "Hola como estas"
    convert(text)