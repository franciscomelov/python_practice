array=[]
def students():
    cals = [cal[1] for cal in array]
    cals = set(cals)
    cals = list(cals)
    cals.sort()
    if len(cals)>1:
        high2 = cals[1]
    else:
        high2 = cals[0]
    names = [name[0] for name in array if high2 in name]
    names.sort()
    for name in names:
        print(name)

def scores(name, score):
    array.append([name, score])


if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores(name, score)
    students()


# https://www.hackerrank.com/challenges/nested-list/problem