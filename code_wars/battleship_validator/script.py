#https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python
def validate_battlefield(field):
    #There should be 20 number 1
    count_of_1 = sum([row.count(1) for row in field])
    if count_of_1 != 20: return False



    for row in field:
        print(row)
    return field
battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

validate_battlefield(battleField)

#1 battleship (size of 4 cells)
# 2 cruisers (size 3)
# 3 destroyers (size 2)
# 4 submarines (size 1). 