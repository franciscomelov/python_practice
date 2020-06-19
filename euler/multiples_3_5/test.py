import time
cache_key =  [5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 50000000, 100000000, 1000000000, 10000000000, 100000000000]

cache = {10: 23, 100: 2318, 1000: 233168, 10000: 23331668, 100000: 2333316668, 1000000: 233333166668, 10000000: 23333331666668, 100000000: 2333333316666668, 1000000000: 233333333166666668, 10000000000: 23333333331666666668, 100000000000: 2333333333316666666668, 5: 3, 50: 543, 500: 57918, 5000: 5829168, 50000: 583291668, 500000: 58332916668, 5000000: 5833329166668, 50000000: 583333291666668}



def get_result(n, begin = 3, count = 0):
    begin_5 = begin
    while True:
        if begin_5%5 == 0:
            break
        else:
            begin_5 +=1
    list_5 = list(range(begin_5,n,5))
    full_list = [n for n in list_5 if n%3 != 0]
    
    begin_3 = begin
    while True:
        if begin_3%3 == 0:
            break
        else:
            begin_3 +=1
    
    list_3 = list(range(begin_3,n,3))
    full_list +=  list_3
    count +=  sum(full_list)
 
    return count

def Multiples_3_5(n):
    # if nis in cache get value
    if n in cache_key:
        return cache.get(n)

    # if new n save it in array_cache
    cache_key.append(n)
    cache_key.sort()

    #if  there is not key below n make normal operation
    if cache_key.index(n) == 0:
        count = get_result(n)
        cache[n] = count
        return count
    
    # if there is values below n start from there instead from 0
    # if the the first en is 100 and then you n is 1000
    # start count from 100 instead form 0
    n_index = cache_key.index(n)
    previous = cache_key[n_index-1]
    count =  get_result(n, previous, cache.get(previous))
    cache[n] = count 
    return count


t0 = time.time()

print("result",Multiples_3_5(1298782908))
""" print("cache_key = ",cache_key)
print("cache",cache) """



print("************")
t1 = time.time()
print("time", t1-t0)







""" 
def get_result(n, begin = 3, count = 0):
    for i in range(begin,n):
        if i%3 == 0 or i%5 == 0:
            count += i
    return count

print(get_result(1000000))
 """
