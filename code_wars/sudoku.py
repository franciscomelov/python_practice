def done_or_not(board):
    line =[1,2,3,4,5,6,7,8,9]
    # Check rows
    for row in board: 
        check_line = list(line) 
        for num_r in row: 
            if num_r in check_line:
                del check_line[check_line.index(num_r)]
        if len(check_line) >0:
            return  'Try again!'

    # Check columns
    for num_column in range(8):
        check_line = list(line)
        for row in board:
            if row[num_column] in check_line:
                del check_line[check_line.index(row[num_column])]
        if len(check_line) > 0:
            return  'Try again!'

    return 'Finished!'


# row -
# column |
print("no")
print(
    done_or_not([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                 [2, 3, 4, 5, 6, 7, 8, 9, 1], 
                 [3, 4, 5, 6, 7, 8, 9, 1, 2], 
                 [4, 5, 6, 7, 8, 9, 1, 2, 3], 
                 [5, 6, 7, 8, 9, 1, 2, 3, 4], 
                 [6, 7, 8, 9, 1, 2, 3, 4, 5], 
                 [7, 8, 9, 1, 2, 3, 4, 5, 6], 
                 [8, 9, 1, 2, 3, 4, 5, 6, 7], 
                 [9, 1, 2, 3, 4, 5, 6, 7, 8]])#'Finished!'
)


""" 
https://www.codewars.com/kata/53db96041f1a7d32dc0004d2/train/python

SUDOKU checker
 """