# https://platzi.com/comunidad/platzicodingchallenge-dia-34-numeros-primos/


primes = [2, 3] #Lista de primos, Primer primo = 2 
def is_prime(test):
    for prime in primes:   #checando sin son divisibles entre algun numero de la lista de primos
        if test%prime==0:
            break
        elif prime > (test/2):
            #No es necesario probar division co n todos losnumeros hasta test-1 
            #solo hasta test /2 
            #por ejemplo si queremos saber si 100 es numero primo
            #solo probamos divisiones has 100/2   50
            # despues del 50 es seguro que no saldra division entera
            primes.append(test)
            break 

def get_primes(nth_prime):
    n = 1
    
    # en primes se iran guardando los primos 
    while True:# Cuando el tamaño de primes sea ==n tengo el nth prime
        # Revizo despues de cada llamada
        #Porque puedo haber acrualizado primes
        is_prime(6*n-1)
        if len(primes) > nth_prime:
            break
        is_prime(6*n+1)
        if len(primes) > nth_prime:
            break
        #Apartir del 3 todos los primos seran el resultado de
        #6*n-1  y 6*n+1 y solo probando los resultados de estas operaciones
        #reduce el numero de calculos
        
        n +=1
    print(primes[nth_prime-1])# imprime el index en nth prime -1 proque empieza en 0

if __name__ == "__main__":
    #n = int(input("hasta que numero quieres buscar primos?: "))
    nth_prime =10000
    get_primes(nth_prime)
