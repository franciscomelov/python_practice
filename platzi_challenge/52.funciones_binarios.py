def dec_bin(num):
    print(bin(num))
    print(bin(num)[2:])
    print("{0:b}".format(num))
    print(f'{num:b}')

num = 102
dec_bin(num)