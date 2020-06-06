# https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem
import time
cache_key =  []
cache = {}

def get_result(n, begin = 3, count = 0):
#COUNT 3
    arr_3 =[]
    begin_3 = begin
    while True:
        if begin_3% 3 == 0:
            break
        else:
            begin_3 += 1
    for i in range(begin_3,n, 3):
        arr_3.append(i)
# COUNT 5
    arr_5 =[]
    begin_5 = begin
    while True:
        if begin_5% 5 == 0:
            break
        else:
            begin_5 += 1
    for i in range(begin_5,n,5):
        arr_5.append(i)

    for i in range(len(arr_5)):
        if not (arr_5[i] in arr_3):
            arr_3.append(arr_5[i])

    return sum(arr_3)

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
    cache[n] = count + cache.get(previous)
    return count + cache.get(previous)


t0 = time.time()
print("result",Multiples_3_5(10))
print("cache_key = ",cache_key)
print("cache",cache)

print("result",Multiples_3_5(100))
print("cache_key = ",cache_key)
print("cache",cache)

print("result",Multiples_3_5(1000))
print("cache_key = ",cache_key)
print("cache",cache)

print("result",Multiples_3_5(10000))
print("cache_key = ",cache_key)
print("cache",cache)

print("result",Multiples_3_5(100000))
print("cache_key = ",cache_key)
print("cache",cache)

print("result",Multiples_3_5(1000000))
print("cache_key = ",cache_key)
print("cache",cache)
print("************")
t1 = time.time()
print("time", t1-t0)




def test(n):
    arr_3 =[]
    for i in range(3,n,3):
        if i%3 == 0:
            arr_3.append(i)

    arr_5 =[]
    for i in range(5,n, 5):
        if i%5 == 0:
            arr_5.append(i)

    for i in range(len(arr_5)):
        if not (arr_5[i] in arr_3):
            arr_3.append(arr_5[i])

    return sum(arr_3)





""" 
cache_key =  [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]
cache = {10: 23, 100: 2318, 1000: 233168, 10000: 23331668, 100000: 2333316668, 1000000: 233333166668, 10000000: 23333331666668, 100000000: 2333333316666668, 1000000000: 233333333166666668}


t = int(input().strip())
for a0 in range(t):
    n = int(input(" numero: ").strip())
    print("result",Multiples_3_5(n))
    print("cache_key = ",cache_key)
    print("cache",cache)
 """



""" 
dict = {1:"uno", 2:"dos", 3:"tres"}
if 4 in dict.keys():
    print("yes")
else:
    print("not")
print(dict.get(1))
 

arr = [1,2,3,4,5,6]
print(0 in arr)
 """