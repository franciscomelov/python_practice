
from datetime import date
from datetime import datetime


def birthday(your_bday):
    your_bday = your_bday.split("-")
    year = datetime.now().year
    your_bday = date(year, int(your_bday[0]), int(your_bday[1]))

    today = date.today()
    days = your_bday - today
    print(days.days,"dias para tu cumpleños")


if __name__ == "__main__":
    your_bday = input("Ingresa tu fecha de cumpleaños: mes-dia: ")
    birthday(your_bday)