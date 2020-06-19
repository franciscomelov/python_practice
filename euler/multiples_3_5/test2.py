

def get_result(n):
    list_3 = list(range(3,n,3))
    list_5 = list(range(5,n,5))
    full_list = [n for n in list_5 if n%3 != 0]
    full_list +=  list_3
    count +=  sum(full_list)

print(get_result(100000000000))

print (583333291666668 == 583333291666668)
