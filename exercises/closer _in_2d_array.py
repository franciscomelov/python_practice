from math import sqrt
board = [
[ 0,  0,  0, -1,  0,  0,  0,  0,  0,  0,],
[ 0, -1,  0,  0,  0,  0,  0, -1,  0,  0,],
[ 0,  0,  0,  0, -1,  0,  0,  0, -1,  0,],
[ 0,  0, -1, -1, -1,  0,  0,  0,  0,  0,],
[ 0,  0,  0,  0,  0,  0,  0,  0, -1, -1]]

def game(x, y):
    shortest = len(board[0]) # shortest distance, starts with the biggest distance
    short_coor = [0, 0] # coordinates of the closer -1 to the point [x, y]

    for i_y, array_y in enumerate(board): # array in y
   
        for i_x, array_x in enumerate(array_y): # array in x
            value = board[i_y][i_x] # Value of each index ,  -1 or 0

            if value == -1: # if it detects a -1 values it saves the coordenates
                
                distance = sqrt((x - i_x)**2 + (y - i_y)**2 ) # formule to check the distance beetwen 2 points
                print("Coordinates:",i_x, i_y, "-- Distance:",distance)
                
                if distance < shortest: # compare the shortes this tance 
                    shortest = distance
                    short_coor[0] = i_x
                    short_coor[1] =i_y
                    

    print(short_coor)

x = 9
y = 0
game(x, y) # espect 4, 2

#There are "problems" if 2 or more coodinates have the same distance from the starting point