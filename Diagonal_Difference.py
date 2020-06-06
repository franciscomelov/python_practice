def diagonalDifference(arr):
    n = len(arr)
    diag_1 = 0
    diag_2 = 0
    for  i in range(n):
        diag_1 += arr[i][i]
        diag_2 += arr[i][abs(i-(n-1))]
    return abs(diag_1 - diag_2)


print(
    diagonalDifference([[11, 2, 4,0,0], [4, 5, 6,0,0], [10, 8, -12,0,0],[11, 2, 4,0,0], [11, 2, 4,0,0]])
)
""" 
sum of 2 diagonal numbers in an array 
1+5+9 = 15
4+5+1 = 6
and return the absolute difference 
6 - 15 = |9|
[1, 2, 4, ]
[4, 5, 6, ]
[1, 8, 9, ]


[11, 2, 4,0,0]
[4, 5, 6, 0, 0]
[10, 8, -12,0,0]
[11, 2, 4,0,0]
[11, 2, 4,0,0]
 """