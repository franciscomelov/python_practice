# https://www.hackerrank.com/challenges/mini-max-sum/problem?h_r=next-challenge&h_v=zen
def miniMaxSum(arr):
    arr.sort()
    mini = sum(arr[:4])
    maxi = sum(arr[1:])
    return f"{mini} {maxi}"

print(
    miniMaxSum([1,3,5,7,9]))

""" 
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers
"""