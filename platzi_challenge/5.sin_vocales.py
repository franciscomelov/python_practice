# -*- coding: utf-8 -*-
# https://platzi.com/comunidad/platzicodingchallenge-dia-5-necesitamos-vocales-4/

def desvocalizador(text):
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚüÜ" #diccionario de vocales
    
    new_text =""
    for l in text:
        if l in vocales:
            continue
        else:
            new_text += l
    #new_text = "".join([l for l in text if l not in vocales])

    print(new_text)

if __name__ == "__main__":
    text = "a b c d e f g h i"
    desvocalizador(text)