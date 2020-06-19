#https://www.hackerrank.com/challenges/array-left-rotation/problem
def left_rot(move, array):
    new_array = array[move:]
    new_array += array[:move]
    return (" ".join(map(str, new_array)))
    


left_rot(4,[1,2,3,4,5]) #5 1 2 3 4 5