# https://platzi.com/comunidad/platzicodingchallenge-dia-26-y-27-ordenando-ando-2-y-3/
import time
import csv


unordered_names = []
with open('names.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        unordered_names.append(', '.join(row))
        
def bubble_sort(names):
    #print(names)
    counter = 0
    ordenado = False # varieble que mientra no este ordenado el array sera falso
    while not ordenado:
        counter += 1
        for i in range(len(names)-1): # ordenar
            if names[i] > names[i+1]: # si el numero a > b  se intercambian a y b van avanzando por el array
                names[i], names[i+1] = names[i+1], names[i]

        # CHECK
        for i in range(len(names)-1):
            if names[i] > names[i+1]:  # si detecta que a > b termina el ciclo de chequeo y vuelve a ordenas
                break
            elif i == len(names)-2:  # si a nunca fue mayor que b y llego al final del array, el array esta ordenado
                ordenado = True # unavez ordenado completamente ordenado == True
    print("-------------------------------------------")
    #print(names)
    print("bubble counter:",counter)

def cocktail_sort(names):
    #print(names)
    counter = 0
    ordenado = False
    index_izq = 0
    index_der = len(names)-1

    while not ordenado:
        #print(names)
        counter += 1
        for i in range(index_izq, index_der): # ordenar de IZQ - DER
            if names[i] > names[i+1]: # 
                names[i], names[i+1] = names[i+1], names[i]

        for i in range(index_der, index_izq, -1): # ordenar de DER - IZQ
            if names[i] < names[i-1]: # si el numero a > b  se intercambian a y b van avanzando por el array
                names[i], names[i-1] = names[i-1], names[i]

        index_izq +=1  # Los indecies se van recorriendo porque ya no es
        index_der -=1  #porque sabesmos que el ultimo y primero estan en su lugar
        print(index_der, index_izq)
        # CHECK
        for i in range(len(names)-1):
            if names[i] > names[i+1]:  # si detecta que a > b termina el ciclo de chequeo y vuelve a ordenas
                break
            elif i == len(names)-2:  # si a nunca fue mayor que b y llego al final del array, el array esta ordenado
                ordenado = True # unavez ordenado completamente ordenado == True
    print(names)
    print("cocktail counter:",counter)


print("------BUBBLE-----")
start_time = time.time()
#bubble_sort(unordered_names)
print("--- %s seconds ---" % (time.time() - start_time))

print("------COCKTAIL-----")
start_time = time.time()
cocktail_sort([0,9,8,7,6,5,4,3,2,1,10,9,8,7,6,55,4,3,2,12,1])
print("--- %s seconds ---" % (time.time() - start_time))
#0.0010018348693847656
