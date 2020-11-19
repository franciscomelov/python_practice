def propina():
    food_list =[] # Guardar lista de platillo
    price_list =[] #guardar lista de precios
    while True: # ciclo para ingresar datos sin limite conocido
        print("")  #un espacio
        food = input("Platillo: ") #preguntar por comida
        if food == "salir":  # si se escribio "salir" terminar ciclo
            break

        price = float(input("Costo: "))  # costo de platillo

        food_list.append(food)  #append platillo y precios al final de los arrays
        price_list.append(price)
    
    subTotal =  sum(price_list)  # Subtotal todos los precios
    tip = round(subTotal * 0.15,2)  # sacar la propina  15%
    total = round(subTotal + tip,2)   # total = subtotal + tip   2 decimales

    for i in range(len(food_list)):    #ciclo para imprimir todos los platillo con si precio
        print(f"{price_list[i]}-----{food_list[i]}")
    print("-----------")
    print(f"Subtotal: {subTotal}")
    print(f"Propina: {tip}")
    print(f"Total: {total}")


if __name__ == "__main__":
    print("Bienvenido. Ingresa tus platillos y el valor de cada uno")
    print("")
    print("Platillo: Sopa")
    print("Costo: 10")
    print("")
    print("Aterminar solo escribe:   salir    en la opcion platillo")

    propina()