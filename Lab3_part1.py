#student name:Nikoo Vali
#student number:83343012

def checkColumn(puzzle: list, column: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param column: the column to check (a value between 0 to 8)

        This function checks the indicated column of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    #To implement
    # Get values from the specified column
    col_values = [puzzle[row][column] for row in range(9)]
    # Check for any invalid values or duplicates
    if any(val < 1 or val > 9 for val in col_values) or len(set(col_values)) != 9:
        print(f"Column {column} not valid")
    else:
        print(f"Column {column} valid")

def checkRow(puzzle: list, row: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param row: the row to check (a value between 0 to 8)

        This function checks the indicated row of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    #To implement
    # Get values from the specified row
    row_values = puzzle[row]
    # Check for any invalid values or duplicates
    if any(val < 1 or val > 9 for val in row_values) or len(set(row_values)) != 9:
        print(f"Row {row} not valid")
    else:
        print(f"Row {row} valid")

def checkSubgrid(puzzle: list, subgrid: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param subgrid: the subgrid to check (a value between 0 to 8)
        Subgrid numbering order:    0 1 2
                                    3 4 5
                                    6 7 8
        where each subgrid itself is a 3x3 portion of the original list
        
        This function checks the indicated subgrid of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    #To implement
    # Calculate starting row and column of the subgrid
    start_row = (subgrid // 3) * 3
    start_col = (subgrid % 3) * 3
    # get values from the specified 3x3 subgrid
    subgrid_values = [puzzle[row][col] for row in range(start_row, start_row + 3) 
                                        for col in range(start_col, start_col + 3)]
    # Check for any invalid values or duplicates
    if any(val < 1 or val > 9 for val in subgrid_values) or len(set(subgrid_values)) != 9:
        print(f"Subgrid {subgrid} not valid")
    else:
        print(f"Subgrid {subgrid} valid")


if __name__ == "__main__":
    test1 = [ [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [1, 4, 3, 8, 6, 5, 7, 2, 9],
              [9, 5, 8, 2, 4, 7, 3, 6, 1],
              [7, 6, 2, 3, 9, 1, 4, 5, 8],
              [3, 7, 1, 9, 5, 6, 8, 4, 2],
              [4, 9, 6, 1, 8, 2, 5, 7, 3],
              [2, 8, 5, 4, 7, 3, 9, 1, 6]
            ]
    test2 = [ [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ]
            ]
    # Test Case 3: Invalid Number Outside Range
    test3 = [
        [6, 2, 4, 5, 3, 9, 1, 8, 7],
        [5, 1, 9, 7, 2, 8, 6, 3, 4],
        [8, 3, 7, 6, 1, 4, 2, 9, 5],
        [1, 4, 3, 8, 6, 5, 7, 2, 9],
        [9, 5, 8, 2, 4, 7, 3, 6, 10],  # Invalid number (10)
        [7, 6, 2, 3, 9, 1, 4, 5, 8],
        [3, 7, 1, 9, 5, 6, 8, 4, 2],
        [4, 9, 6, 1, 8, 2, 5, 7, 3],
        [2, 8, 5, 4, 7, 3, 9, 1, 6]
    ]


    # Test Case 4: Valid but Incomplete Board (for partial validation)
    test4 = [
        [6, 0, 4, 5, 3, 9, 1, 8, 7],
        [5, 1, 9, 7, 2, 8, 6, 3, 4],
        [0, 3, 7, 6, 1, 4, 2, 9, 5],
        [1, 4, 3, 8, 6, 5, 7, 0, 9],
        [9, 5, 8, 2, 4, 7, 3, 6, 1],
        [7, 6, 2, 3, 9, 1, 4, 5, 8],
        [3, 7, 1, 9, 5, 6, 8, 4, 2],
        [4, 9, 6, 1, 8, 2, 5, 7, 3],
        [2, 8, 5, 4, 7, 3, 9, 1, 6]
    ]  # 0 indicates incomplete values

    # Test Case 5: All Zeros (invalid board)
    test5 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]  # Invalid board, all cells are zero

    # Test Case 6: Valid Sudoku Board with Different Configurations
    test6 = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]  # All numbers are unique, valid configuration

    
    testcase = test1
    SIZE = 9

    for col in range(SIZE):  #checking all columns
        checkColumn(testcase, col)
    for row in range(SIZE):  #checking all rows
        checkRow(testcase, row)
    for subgrid in range(SIZE):   #checking all subgrids
        checkSubgrid(testcase, subgrid)