# https://platzi.com/comunidad/platzicodingchallenge-calculadora-v2/

def mul(op):
    while "*" in op :
        index = op.index("*")
        a ,b = op[index-1], op[index+1]
        op[index] = int(a) * int(b)
        del op[index-1]
        del op[index]
    return op


def sum(op, ):
    while "+" in op :
        index = op.index("+")
        a ,b = op[index-1], op[index+1]
        op[index] = int(a) + int(b)
        del op[index-1]
        del op[index]
    return op

def calc(op):
    op = op.split()
    
    while len(op)>1:
        if "*" in op: op = mul(op)

        if "+" in op: op = sum(op)

    print(op)

#op = input("Ingresa tu operacion: ")
op = "100 + 999 * 0 + 100 + 95 + 55 + 66 * 0 + 1 * 66 * 5 + 11"
calc(op)