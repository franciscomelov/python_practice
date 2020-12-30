primes = [2, 3]

def is_prime(test):
    for prime in primes:   #checando sin son divisibles entre algun numero de la lista de primos
        if test%prime==0:
            break
        elif prime > (test/2):
            primes.append(test)
            break 

def get_primes(number):
    n = 1
    
    while True:
        is_prime(6*n-1)
        if 6*n-1 >= number:
            break
        is_prime(6*n+1)
        if 6*n+1 >= number:
            break
        n +=1

def b_prime_factor(t, n):
    factor =[]
    big_factor=None
    for number in n: # iterate array n
        for _ in range(t): #search prime factors
            
            if number > primes[-1]:get_primes(number) # if true get primes below number

            if number in primes:
                factor.append(number)
                break
            
            else:
                for prime in primes:
                    if number%prime==0:
                        big_factor=prime
                    if prime > number/3:
                        break
                factor.append(big_factor)
                break

    for num in factor:
        print(num)

t = 3
n=[17,50, 10, 10000, 55551, 111111]

b_prime_factor(t, n)



# take a number from n
# if number is prime return number
# else get the biggest factor prime number/ biggest prime == 2