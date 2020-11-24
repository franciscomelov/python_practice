mensaje='''Ingresa tu texto de acuerdo al siguiente diccioario:
2 ABC
3 DEF
4 GHI
5 JKL
6 MNO
7 PRS
8 TUV
9 WXY
Donde si desea escribir Ej S debe ingresar el número 7 y
las veces de tecleado será igual 3 '''
sms=[]
numero2=['A','B','C']
numero3=['D','E','F']
numero4=['G','H','I']
numero5=['J','K','L']
numero6=['M','N','O']
numero7=['P','R','S']
numero8=['U','T','V']
numero9=['W','X','Y']
numeros=[numero2,numero3,numero4,numero5,numero6,numero7,numero8,numero9]
print(mensaje)
pregunta='y'
while pregunta=='y':
    entrada_teclado=int(input('Ingrese un número del 2 al 9: '))
    veces_tecla=int(input('Ingrese cuantas veces presionar esa tecla: '))
    pregunta=input('Desea ingresar más letras a tu palabra? Y/N ')
    tecla=numeros[entrada_teclado-2]
    letrasms=tecla[veces_tecla-1]
    sms.append(letrasms)
sms="".join(sms)
print(sms)