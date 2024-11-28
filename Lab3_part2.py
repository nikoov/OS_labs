#student name:Nikoo Vali
#student number:83343012

import multiprocessing

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
    # Define the test puzzle
    puzzle = [[6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ]
            ]
    

    # List to hold all processes
    processes = []

    # Create and start processes for checking all rows
    for row in range(9):
        p = multiprocessing.Process(target=checkRow, args=(puzzle, row))
        processes.append(p)
        p.start()

    # Create and start processes for checking all columns
    for col in range(9):
        p = multiprocessing.Process(target=checkColumn, args=(puzzle, col))
        processes.append(p)
        p.start()

    # Create and start processes for checking all subgrids
    for subgrid in range(9):
        p = multiprocessing.Process(target=checkSubgrid, args=(puzzle, subgrid))
        processes.append(p)
        p.start()

    # Ensure all processes complete before exiting
    for process in processes:
        process.join()

