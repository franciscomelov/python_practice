# https://www.hackerrank.com/challenges/finding-the-percentage/problem

from math import floor

def students_everage(students_list, query_name):
    everage = sum(students_list[query_name]) / len(students_list[query_name])
    
    print("%.2f"%(everage))

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    students_everage(student_marks, query_name)


https://thepythonguru.com/python-string-formatting/