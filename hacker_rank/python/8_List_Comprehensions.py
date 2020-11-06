#https://www.hackerrank.com/challenges/list-comprehensions/problem
def list_com(x,y,z,n):
            #i  j k
    lista = [[i,j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    lista = [check for check in lista if sum(check) != n]
    print(lista) 

    #lista = [[i,j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i,j,k]) != n]


x=2
y=2
z=2
n=2
list_com(x,y,z,n)
