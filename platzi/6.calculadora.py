""" 
+  -  *  /
 """
 # https://platzi.com/comunidad/platzicodingchallenge-calculadora-piedra-papel-o-tijera/
def calc(a, op, b):
    
    if op == "+": return a + b
    elif op == "-": return a - b
    elif op == "*": return a * b
    elif op == "/": return a / b


if __name__ == "__main__":
    a = -3
    op = "+"
    b = 3
    result = calc(a, op, b)
    print(result)

