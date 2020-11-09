def recursion(text, times):
    if times <= 1:
        print(text)
        return
    print(text)
    return recursion(text, times-1)

if __name__ == "__main__":
    text = input("Ingresa un mensaje: ")
    times = int(input("Numero de repeticiones: "))
    text = recursion(text, times)
    