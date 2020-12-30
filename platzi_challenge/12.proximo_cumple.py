from datetime import date


def birthday(your_bday):
    your_bday = your_bday.split("-") #separa your_bday en array [mes, dia]
    your_bday = date(int(your_bday[0]), int(your_bday[1]), int(your_bday[2])) # date(year, month, day) convierte num to real date
    today = date.today()  # guarda en today la fecha actual
    days = (your_bday - today).days  # resta a la fecha de tu cumpleños la fecha actual,  #days regresa fecha y hora con .days solo regresa dias



    return days ," dias para tu cumpleños"


if __name__ == "__main__":
    your_bday = "2021-12-22" #mes - dia
    days = birthday(your_bday)
    print(days)


# from datetime import date


# def birthday(your_bday):
#     your_bday = your_bday.split("-") #separa your_bday en array [mes, dia]
#     year = date.today().year #guarda en year el año actual
#     your_bday = date(year, int(your_bday[0]), int(your_bday[1])) # date(year, month, day) convierte num to real date
#     today = date.today()  # guarda en today la fecha actual
#     days = (your_bday - today).days  # resta a la fecha de tu cumpleños la fecha actual,  #days regresa fecha y hora con .days solo regresa dias

#     if days < 0: 
#         your_bday = str(your_bday).split("-")
#         your_bday = date(int(year) +1, int(your_bday[1]), int(your_bday[2]))
#         days = (your_bday - today).days
#         return days , " dias para tu cumpleños"

#     return days ," dias para tu cumpleños"


# if __name__ == "__main__":
#     your_bday = "1-13" #mes - dia
#     days = birthday(your_bday)
#     print(days)



