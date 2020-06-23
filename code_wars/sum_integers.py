def digital_root(n): 
    #n = list(str(n))
    n = [int(x) for x in list(str(n))]
    if len(n) ==1:
        return n[0]
    return digital_root(sum(n))

print(digital_root(1))
#2

print(54%7)

""" 
Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.
942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
"""
""" 
def digital_root(n):
    return n%9 or n and 9 """