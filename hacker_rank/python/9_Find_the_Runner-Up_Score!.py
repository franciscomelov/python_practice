# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?h_r=next-challenge&h_v=zen
def runner_up(n, arr):
    arr = sorted(set(arr))
    second_place = arr[len(arr)-2:len(arr)-1]
    print(second_place[0])
    #print( sorted(set(arr))[len(set(arr))-2:len(set(arr))-1][0] )

n =5
arr = [1,2,3,4,3,2,1,6,5]
runner_up(n,arr)