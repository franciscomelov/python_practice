cache ={}
def fibonacci(n):
    memo = [0,1, 1]
    def do(n):
        if n == len(memo):
            memo.append(memo[n-1] + memo[n-2])
            return memo[n]
        if n in memo:
            return memo[n]
        return do(n - 1) + do(n - 2)

    if n in cache:
        return cache[n]
    else:
        result = do(n)
        cache[n] = result

    return result


print(fibonacci(70))#, 190392490709135)
print(" ")
print(fibonacci(60))#, 1548008755920)
print(" ")
print(fibonacci(50))#, 12586269025)
