""" 
Given to array ([1,2,3],[3,2,1]) with 3 numbers compare a[0] b[0] / a[1] b[1] / a[2] b[2]
if a[n] > b[n]  give 1 point to a
if b[n] > a[n]  give 1 pint to b
if b[n] == a[n] don't give pint
return an array [<point for a>,<pints for b>] 
 """

def compareTriplets(a, b):
    result =[0,0]
    for i in range(3):
        
        if a[i] > b[i]:
            result[0] += 1
        elif b[i] > a[i]:
            result[1] += 1
    return result

print(
    compareTriplets([1,3,3],[3,2,1])
)



