def stair(n):
    spaces = n-1
    for i in range(1, n+1):
        print( spaces * " " + "#" * i)
        spaces -= 1


stair(6)

     #
    ##
   ###
  ####
 #####
######
