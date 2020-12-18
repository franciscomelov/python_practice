#https://nedbatchelder.com/blog/200712/human_sorting.html
from random import randint
def generador(n):
    number = lambda : randint(0,255) # anonymouus function para crear numeros aleatorios, no en una variable por que se repetiria
    ip_list = []

    for _ in range(n):
        pass
        ip_list.append(f'{number()}.{number()}.{number()}.{number()}')

    ip_list = sorted(ip_list)
    for i in ip_list:
        print(i)
        pass


    print("original list size: ",len(ip_list))
    print("original list size: ",len(set(ip_list)))




n=10
generador(n)