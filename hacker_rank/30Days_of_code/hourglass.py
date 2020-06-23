#https://www.hackerrank.com/challenges/2d-array/problem
def hourglassSum(arr):
    hg_arr = []

    for d in range(len(arr)):#arriba-abajo
        if d > len(arr)-3:
            break
        for i in range(len(arr[0])): # Izquierda -derecha 
            # hourglass
            if i > len(arr[0])-3:
                break
        
            arr_2 = ( arr[d][i:i+3] )     ###
            arr_2.append( arr[d+1][i+1] )  #
            arr_2 += ( arr[d+2][i:i+3])   ### 
            hg_arr.append(arr_2)
    
    max_sum = sum(hg_arr[0])
    for ar in hg_arr:
        if sum(ar) > max_sum:
            max_sum = sum(ar) 
    
    return max_sum

        

    
 
""" 
print(
    hourglassSum([
      [1, 1, 1, 0, 0, 0,0],
      [0, 1, 0, 0, 0, 0,0], 
      [1, 1, 1, 0, 0, 0,0], 
      [0, 0, 2, 4, 4, 0,0], 
      [0, 0, 0, 2, 0, 0,0], 
      [0, 0, 1, 2, 4, 0,0],
      [0, 0, 1, 2, 0, 0,0]])
)
 """
print(
    hourglassSum([
      [ 0, -4, -6, 0, -7, -6],
      [-1, -2, -6, -8, -3, -1], 
      [-8, -4, -2, -8, -8, -6], 
      [-3, -1, -2, -5, -7, -4], 
      [-3, -5, -3, -6, -6, -6], 
      [-3, -6, 0, -8, -6, -7]])
)
