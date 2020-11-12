from random import randint
def game():
    atacante = sorted([randint(1,7) for x in range(3)], reverse=True)
    defensor = sorted([randint(1,7) for x in range(2)], reverse=True)

    print("Atacante:",atacante)
    print("Defensor:",defensor)

    for i in range(2):
        if atacante[i] > defensor[i]:
            diferencia = atacante[i] -defensor[i]
            print(f"Defensor pierde: {diferencia} ({atacante[i]} es mayor que {defensor[i]})")
        elif defensor[i] > atacante[i]:
            diferencia = defensor[i] -atacante[i]
            print(f"Atacante pierde: {diferencia} ({defensor[i]} es mayor que {atacante[i]})")
        else:
            print(f"Empate: ({defensor[i]} y {atacante[i]} son iguales)")

if __name__ == "__main__":
    game()