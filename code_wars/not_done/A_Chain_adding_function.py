#https://www.codewars.com/kata/539a0e4d85e3425cb0000a88/train/python


def funcwrapper(y):
    def addone(x):
        return x + y + 1
    return addone

result = funcwrapper(3)(2)
print (result)


def funcwrapper(y):
    def addone(x):
        def addother(w):
            return w + y + x
        return addother
    return addone

result = funcwrapper(3)(2)(1)
print(result)

