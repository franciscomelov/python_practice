

def contador(text, word):
    # text=open("texto.txt", "r")
    # arr = text.read()   # lee el archivo 
    # print(arr.count(word)) #usando funcion count

    #haciendo manual mente
    text=open("texto.txt", "r", encoding="UTF8")  # encoding="UTF8" para reconec acentos y ñ
    arr = text.read().split() # lee el archivo y lo separa en array
    counter =0
    for w in arr:
        print(w, word)
        if w == word:
            
            counter += 1
    print(counter)



text = "texto.txt"
word = "ñ"
contador(text, word)