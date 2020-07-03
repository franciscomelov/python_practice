def max_sequence(arr):

    if len(arr) == 0 or len([x for x in arr if x >0]) == 0:
        return 0

    biggest = arr[0]
    
    for num in range(len(arr)):
        roll = num +1
        while roll != len(arr)+1:
            compare =sum(arr[num:roll])

            if compare >biggest:
                biggest = compare   
                print("biggest ",compare,arr[num:roll])
            print(compare,arr[num:roll])

            roll +=1

    return biggest





print(max_sequence([-2,-13,-1])) #6


""" 
https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
 """