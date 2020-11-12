
def get_primes(n):
    primes = [2] #Lista de primos, Primer primo = 2 
    
    for test in range(2,n+1):# probando numeros de 2 a n

        for prime in primes:   #checando sin son divisibles entre algun numero de la lista de primos
            if test%prime==0:
                break
            elif prime == primes[len(primes)-1]: #si llego al final de la lista y no ha sido divisible lo añade a la lista de primos
                primes.append(test)
    print(primes)

if __name__ == "__main__":
    #n = int(input("hasta que numero quieres buscar primos?: "))
    n =1000
    get_primes(n)