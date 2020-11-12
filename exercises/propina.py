def propina():
    print("Bienvenido. Ingresa tus platillos y el valor de cada uno")
    print("")
    print("Platillo: Sopa")
    print("Costo: 10")
    print("")
    print("Aterminar solo escribe:   salir    en la opcion platillo")
    food_list =[]
    price_list =[]
    while True:
        print("")
        food = input("Platillo: ")
        if food == "salir":
            break

        price = float(input("Costo: "))

        food_list.append(food)
        price_list.append(price)
    
    subTotal =  sum(price_list)
    tip = round(subTotal * 0.15,2)
    total = round(subTotal + tip,2.)

    for i in range(len(food_list)):
        print(f"{price_list[i]}-----{food_list[i]}")
    print("-----------")
    print(f"Subtotal: {subTotal}")
    print(f"Propina: {tip}")
    print(f"Total: {total}")


if __name__ == "__main__":
    propina()