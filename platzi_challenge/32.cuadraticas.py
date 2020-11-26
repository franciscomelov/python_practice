# https://platzi.com/comunidad/platzicodingchallenge-32-ecuaciones-cuadraticas/
from math import sqrt
 
# simplemente se conbierte la formula a codigo
def formula_general(a, b, c):
    x1 = (-b + sqrt(b**2 - 4*a*c)) / ( 2*a)   # Con suma
    x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)    # con resta
    print(f'X1 = {x1}')
    print(f'X2 = {x2}')


print("""
Teniendo el siguiente formato: ax**2 + bx + c Ingresa el valor de a, b, c:
""")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
a=4
b=3
c=-22
formula_general(a, b, c)

