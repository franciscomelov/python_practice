#https://www.codewars.com/kata/55f4a44eb72a0fa91600001e/train/python
def create_message(s):
    dicti ={}
    count = 0
    def other(a):
        return create_message(s)
    for i in other:
        dict[count] = i
        count += 1
    print(dict)


    return other

print(create_message(1)(2)(3))
    


# https://oswalt.dev/2015/05/double-parentheses-in-python/
""" 
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


 """