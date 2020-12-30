def test_pass (password):
    counter = 0
    if any(char.islower() for char in password): counter+=1
    if any( char.isupper() for char in password): counter+=1
    if any( char.isdigit() for char in password): counter+=1
    if any(not char.isalnum() for char in password): counter+=1 #special char
    if len(password) >= 8: counter+=1

    if counter <= 2: print("password Insegura")
    elif counter <= 4: print("password Medianamente segura")
    else: print("password segura")

    print(counter)


password = "abc123bdddvA#"
test_pass(password)


""" 
Incluir al menos una letra minúscula
Incluir al menos una letra mayúscula
Incluir al menos un número
Incluir al menos un caracter especial
Tener una longitud mínima de 8 caracteres

Se evaluará la contraseña con las siguientes características:
Insegura: cumple con solo 2 o menos parámetros
Medianamente segura: cumple de 3 o 4 parámetros
Segura: cumple con todos los parámetros
 """