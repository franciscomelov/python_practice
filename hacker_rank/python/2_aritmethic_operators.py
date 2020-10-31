# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
# cambiar a f"{}" - f-string
def run(a,b):
    print("""{}
{}
{}
    """.format(a+b,a-b,a*b))

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    run(a,b)