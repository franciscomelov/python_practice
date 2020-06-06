#https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem
import math

def check(primes, test):
    search = list(primes[0:math.ceil(len(primes) / 3)])

    for j in search:
        if  test%j == 0:
            break
        if j== search[len(search)-1]:
            primes.append(test)

        #if (primes[math.floor(len(primes) / 2)]) < j:
         #   print("------")
    


    return primes

def n_prime(n):
    primes = [2,3]
    i= 1
    while True:
        if len(primes) < n:
            primes = check(primes, 6 * i - 1)
        else:
            break

        if len(primes) < n:
            primes = check(primes, 6 * i + 1)
        else:
            break
        i +=1
  
    return primes[n-1]



print(n_prime(100011))

