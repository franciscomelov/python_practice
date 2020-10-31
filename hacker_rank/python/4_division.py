def run(a,b):
    return """{}
{}
    """.format(a//b, a/b)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    result = run(a, b)
    print(result)


#https://www.hackerrank.com/challenges/python-division/problem?h_r=next-challenge&h_v=zen