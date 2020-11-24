#https://platzi.com/comunidad/platzicodingchallenge-dia-28-codigo-morse-y-29-telefono/
morse_code= {
    "A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-..",
    "E":".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",
    "0":"-----",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    ",":"--..--"
}

def morse_to_letters(text):
    #solo traduce
    text = [letter for letter in text if letter != " "]  #Separa el texto en unarray por letra
    morse = [morse_code[letter] for letter in text] #del dccionario morse_code lee el codigo que es igual a cda letra
    print(" ".join(morse)) # une el codigo en un solo string
    # .... --- .-.. .- -.-. --- -- --- . ... - .- ...

    # formato de traductor
    morse = ""
    text = text.split()  #separa por palabra
    for word in text: # Ciclo sobre cada palabra del array text
        for letter in word: # ciclo sobre cada letra del word
            morse+= morse_code[letter] + " "  #convierte cada palabra y le da un espacio
        morse+="/"  # aggrega una diagonal al final de cada palabra
        #.... --- .-.. .- /-.-. --- -- --- /. ... - .- ... /
    print(morse)
text = "HOLA COMO ESTAS"
morse_to_letters(text)

# .... --- .-.. .- -- ..- -. -.. ---
# .... --- .-.. .- -- ..- -. -.. ---