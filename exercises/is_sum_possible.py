"""
Given an array of integer and a value, determaine if there are two integers
in the array whose sum is equal to the given values return True or False
"""


def solution(array_of_integers, value):
    if len(array_of_integers) < 2:
        return False

    current_sum = array_of_integers[0] + array_of_integers[-1]
    if current_sum == value:
        return True
    elif current_sum > value:
        return solution(array_of_integers[0:-1], value)
    elif current_sum < value:
        return solution(array_of_integers[1:], value)


nums = [2, 7, 11, 15]
target = 18
a = solution(nums, target)
print(a)


nums = [2, 7, 11, 15]
target = 90
print(solution(nums, target))
