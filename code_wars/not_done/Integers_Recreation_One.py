from math import sqrt, floor

def list_squared(m, n):
    
    squared = []    
    for x in range(m, n+1):
        check = [x**2]

        """         
        for mod_0 in range(math.floor(x/2),0,-1):
            print(x, mod_0,x%mod_0)
            if x%mod_0 == 0:
                check.append(mod_0 **2)
                 """
        check +=[mod_0**2 for mod_0 in range(floor(x/2),0,-1) if x%mod_0 ==0]
        print(x, [mod_0 for mod_0 in range(floor(x/2),0,-1) if x%mod_0 ==0])
        check =sum(check)
        if sqrt(check) %1 ==0:
            squared.append([x,check])
    
    return squared

    


print(list_squared(1,260))

#https://www.codewars.com/kata/55aa075506463dac6600010d/train/python
# Works but it take a lot of time