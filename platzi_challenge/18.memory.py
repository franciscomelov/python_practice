# https://platzi.com/comunidad/platzicodingchallenge-memory-parte-1/

from random import randint

code ="#$%()/&"

def get_code(code):
    new_code =""
    
    for _ in range(4):
        new_code += code[randint(0,len(code)-1)]
    print(new_code)

    # other_code = [code[randint(0,len(code)-1)] for _ in range(4)]
    # print("".join(other_code))


get_code(code)