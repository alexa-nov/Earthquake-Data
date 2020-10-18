def get_cages():
    cages = []
    num_cages = int(input("Number of cages: "))
    for val in range (0, num_cages):
        cage_input = input("Cage number %d : " %(val)).split()
        cage_int = [int(val) for val in cage_input]
        cages.append(cage_int)
    return (cages)

#Check Individual Row
def check_row(row):
    seen_so_far_rows = []
    for val in row:
        if val not in seen_so_far_rows:
            seen_so_far_rows.append(val)
        elif val == 0:
            seen_so_far_rows.append(val)
    if len(seen_so_far_rows) == len(row):
        return True
    else:
        return False

#Check All Rows
def check_rows_valid(puzzle):
    for row in puzzle:
        check_row(row)
        if check_row(row) == False:
            return False
    return True

#Check Individual Column
def check_column(column):
    seen_so_far_columns = []
    for val in column:
        if val not in seen_so_far_columns:
            seen_so_far_columns.append(val)
        elif val == 0:
            seen_so_far_columns.append(val)
    if len(seen_so_far_columns) == len(column):
        return True
    else:
        return False        

#Check All Columns
def check_columns_valid(puzzle):
    all_columns = [[column[0] for column in puzzle],
                   [column[1] for column in puzzle],
                   [column[2] for column in puzzle],
                   [column[3] for column in puzzle],
                   [column[4] for column in puzzle]]
    for column in all_columns:
        check_column(column)
        if check_column(column) == False:
            return False
    return True

#Check Individual Cage
def check_cage(cage, puzzle):
    total = 0
    is_cage_partial = False
    for val in cage[2 : 2 + cage[1]]:
        total = total + puzzle[val // 5][val % 5]
        if puzzle[val // 5][val % 5] == 0:
            is_cage_partial = True
    if is_cage_partial == True:
        if total < cage[0]:
            return True
        else:
            return False
    elif is_cage_partial == False:
        if total == cage[0]:
            return True
        else:
            return False

#Check All Cages
def check_cages_valid(puzzle, cages):
    for cage in cages:
        if check_cage(cage, puzzle) == False:
            return False
    return True

#Check Valid
def check_valid(puzzle, cages):
    if check_rows_valid(puzzle) == True and check_columns_valid(puzzle) == True and check_cages_valid(puzzle, cages) == True:
        return True
    else:
        return False

#Formats Puzzle Print
def puzzle_print(puzzle):
    for list_of_list in puzzle:
        print (' '.join(str(num) for num in list_of_list))
