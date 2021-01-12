from typing import Literal


def to_int(num):
    # num = eval(num) # Built in fuction
    # print(num, type(num))

    try:
        num = int(num)
    except:
        num = float(num)
    print(num, type(num))
    
    (num)
num = "14.195"
to_int(num)
