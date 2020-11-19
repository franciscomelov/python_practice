from datetime import date
from datetime import datetime


def birthday(your_bday):
    your_bday = your_bday.split("-") #separa your_bday en array [mes, dia]
    year = datetime.now().year #guarda en year el año actual
    your_bday = date(year, int(your_bday[0]), int(your_bday[1])) # date(year, month, day) convierte num to real date

    today = date.today()  # guarda en today la fecha actual
    days = (your_bday - today).days  # resta a la fecha de tu cumpleños la fecha actual,  #days regresa fecha y hora con .days solo regresa dias
    if days < 0: days = days +364 #si yapaso el cumpleños añade 364 dias para el siguiente año 
    print(days,"dias para tu cumpleños")


if __name__ == "__main__":
    your_bday = input("Ingresa tu fecha de cumpleaños: mes-dia: ")
    birthday(your_bday)