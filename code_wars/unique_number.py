def find_uniq(arr):
    return [x for x in set(arr) if arr.count(x) ==1][0]


find_uniq([ 3, 10, 3, 3, 3 ]) #10

""" 
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""