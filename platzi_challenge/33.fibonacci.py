# https://platzi.com/comunidad/platzicodingchallenge-dia-33-fibonacci-de-10000/


def n_fibonacci(n):   
    #fib_   = n-1
    #fib    = n

    fib_ =0
    fib = 1

    for _ in range(n):  # ciclo hasta llegar a n
        fib_ ,fib = fib, fib_ +fib    
        # Los valores se vas recorriendo para f = n-1 + n
        # fib_ toma el valor de fib 
        # y fib toma el valor de la nueva suma
        # asi hasta llegar a n
    
    print(fib_)  # se toma fib_ porque fib serie 1 despues de n


n = 10
n_fibonacci(n)

"""
nth   0  1   2    3    4     5   6    7   8   9   10
fib   0  1   1    2    3     5   8    13  21  34  55

"""