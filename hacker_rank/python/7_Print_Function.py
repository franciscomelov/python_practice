# https://www.hackerrank.com/challenges/python-print/problem
def numbers(n):
    line = ""
    for i in range(1, n+1):
        line += str(i)
    print(line)

numbers(3)