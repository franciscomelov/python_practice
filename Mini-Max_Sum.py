# https://www.hackerrank.com/challenges/mini-max-sum/problem?h_r=next-challenge&h_v=zen
def miniMaxSum(arr):
    arr.sort()
    mini = sum(arr[:4])
    maxi = sum(arr[1:])
    return mini, maxi

print(
    miniMaxSum([1,3,5,7,9]))