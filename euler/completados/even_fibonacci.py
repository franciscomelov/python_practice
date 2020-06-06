# https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem

def fibonaci(n):
    arr = [1,2]
    for i in range(n):
        if (arr[i] + arr[i+1]) > n:
            break
        arr.append(arr[i] + arr[i+1])
    return arr


def fibo_even(n):
    arr = fibonaci(n) 
    sum= 0
    for i in arr:
        if i%2 == 0:
            sum += i
    return sum
    

""" 
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(fibo_even(n))
 """

print(fibo_even(10000000))

""" 
create a fibonaci serie the las number should be smaller tha "n"
n = 8
[1,2,3,5]

n = 10
[1,2,3,8]

return the sum of the even numbers
 """