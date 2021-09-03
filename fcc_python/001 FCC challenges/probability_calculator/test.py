from random import randint


def my_function(**kargs):
    contents =[]
    #print([name for name, number in kargs.items() for number in range(number)])
    print("*****")

    for name, number in kargs.items():
        for _ in range(number):
            contents.append(name)
    
    print(contents)

    for _ in range(20):
        idx = randint(0,len(contents)-1)
        print(contents[idx], idx)

#my_function(blue=3,red=2,green=6, pink=1)
a=["red", "blue", "red", "green" ]
b=["red", "blue"]



dict_a ={}
print([])
for ball in a:
    dict_a[ball] = dict_a.get(ball, 0) +1

print(dict_a)