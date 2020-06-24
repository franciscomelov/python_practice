def array_diff(a, b):
    print("a : ",a)
    for num in b:
        while num in a :
            a.remove(num)
    # return [x for x in a if x not in b]
    return a

array_diff([], [5])

""" 
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
"""