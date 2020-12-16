def sumando(total):
    num = input("Ingresa un numero: ")
    if num =="0" or num == "": #Si escribes 0 ó solo das enter termina el programa
        print("Tola = ",total)
        return
    sumando(total+int(num)) #se vuelve allamar a si misma sumando el valor de num total+=num

total = 0
sumando(total)