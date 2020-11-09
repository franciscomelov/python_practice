def convert(hours, minutes):
    minutes += hours * 60
    seconds = minutes *60
    print(seconds)

if __name__ == "__main__":
    hours = int(input("Ingresa las horas: "))
    minutes = int(input("Ingresa los minutos: "))
    convert(hours, minutes)