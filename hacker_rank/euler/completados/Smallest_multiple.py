# hackerrank.com/contests/projecteuler/challenges/euler005/problem

def sm_ml(n):
    count = 0
    state = False
    while not state:
        count += n
        for i in range(1,n+1):
            if count%i != 0:
                break
            if i==n:
                state = True
    return count
    

print(sm_ml(3))
    
