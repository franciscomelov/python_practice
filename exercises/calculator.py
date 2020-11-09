
def calculator(a,op,b):
    if op == "+":
        return a + b
    if op == "-":
        return a -b
    if op == "*":
        return a * b
    if op == "/":
        return a / b
    if op == "^":
        return a ** b
    if op == "r":
        return b ** (1. / a)


if __name__ == "__main__":
    print(""" 
+ = suma                - = resta
* = multiplicacion      / = division
^ = potencia            r = raiz
""")
    a = float(input("primer digito: "))
    op = input("Operancion: ")
    b = float(input("segundo digito: "))
    result = calculator(a,op,b)
    print(result)

