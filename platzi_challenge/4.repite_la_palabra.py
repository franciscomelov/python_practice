# https://platzi.com/comunidad/platzicodingchallenge-dia-4-repite-la-palabra/

def repetidor(text, n):
    print(f'{n}. {text}') # String format para mostra el valor
    if n ==1: # una vez n ==1 termina, para evitar un bucle infinito
        return 
    return repetidor(text, n-1)

if __name__ == "__main__":
    text = "Hola"
    n = 5
    repetidor(text, n)
