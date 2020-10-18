"""
Checks Directions
"""

#Checks Forward
def forward(puzzle, words):
    forward = []
    for word in words:
        for i in range(len(puzzle)):
            if puzzle[i].find(word) != -1:
                word_found = [word, "(FORWARD)", i, puzzle[i].find(word)]
                forward.append(word_found)
    return forward


#Check Backward
def backward(puzzle_str, words):
    rows = format_rev_rows(puzzle_str)
    backward = []
    for word in words:
        for i in range(len(rows)):
            if rows[i].find(word) != -1:
                word_found = [word, "(BACKWARD)", i, len(rows) - rows[i].find(word) - 1]
                backward.append(word_found)
    return backward


#Checks Downward
def downward(puzzle, words):
    downward = []
    columns = format_col(puzzle)
    for word in words:
        for i in range(len(columns)):
            if columns[i].find(word) != -1:
                word_found = [word, "(DOWN)", columns[i].find(word), i]
                downward.append(word_found)
    return downward


#Checks Upward
def upward(puzzle, words):
    columns = format_rev_col(puzzle)
    upward = []
    for word in words:
        for i in range(len(columns)):
            if columns[i].find(word) != -1:
                word_found = [word, "(UP)", len(columns) - columns[i].find(word) - 1, i]
                upward.append(word_found)
    return upward


def diagonal(puzzle, words):
    diagonals = format_diagonal(puzzle)
    diagonal = []
    for word in words:
        for i in range(len(diagonals)):
            if diagonals[i].find(word) != -1:
                if i <= 9:
                    word_found = [word, "(DIAGONAL)", i + diagonals[i].find(word), diagonals[i].find(word)]
                    diagonal.append(word_found)
                else:
                    word_found = [word, "(DIAGONAL)", diagonals[i].find(word), i - 9 + diagonals[i].find(word)]
                    diagonal.append(word_found)
    return diagonal

"""
Puzzle formatting
"""

#Converts puzzle into diagonal (down right)
def format_diagonal(puzzle):
    all_diagonals_1 = []
    all_diagonals_2 = []
    for row in range(len(puzzle)):
        one_diagonal_row = []
        for i in range(10 - row):
            one_diagonal_row.append(puzzle[row + i][i])
        all_diagonals_1.append(''.join(one_diagonal_row))
    for col in range(1,len(puzzle)):
        one_diagonal_col = []
        for i in range(10 - col):
            one_diagonal_col.append(puzzle[i][col + i])
        all_diagonals_2.append(''.join(one_diagonal_col))
    all_diagonals = all_diagonals_1 + all_diagonals_2
    return all_diagonals

#Converts puzzle into list of strings (by reverse column)
def format_rev_col(puzzle):
    columns = format_col(puzzle)
    reverse = []
    res = []
    for val in columns:
        reverse.append(val[::-1])
    return reverse

#Converts puzzle into list of strings (by column)
def format_col(puzzle):
    res = []
    all_columns = [[column[0] for column in puzzle],
                   [column[1] for column in puzzle],
                   [column[2] for column in puzzle],
                   [column[3] for column in puzzle],
                   [column[4] for column in puzzle],
                   [column[5] for column in puzzle],
                   [column[6] for column in puzzle],
                   [column[7] for column in puzzle],
                   [column[8] for column in puzzle],
                   [column[9] for column in puzzle]]
    for column in all_columns:
        res.append(''.join(column))
    return res

#Converts puzzle into list of strings (by reverse row)
def format_rev_rows(puzzle_str):
    reverse = []
    res = []
    for i in range(len(puzzle_str)-1, -1, -1):
        reverse.append(puzzle_str[i])
    reverse_str = ''.join(reverse)
    puzzle_convert = [(reverse_str[i:i+10]) for i in range (0, len(reverse_str), 10)]
    for i in range(len(puzzle_convert)):
        res.append(puzzle_convert[9-i])
        i -= 1
    return res

#Converts puzzle into list of strings (by row)
def format_rows(puzzle_str):
    return [(puzzle_str[i:i+10]) for i in range (0, len(puzzle_str), 10)]
 
#Converts words into list of strings
def format_words(words_str):
    return words_str.split()

#Formats printed puzzle
def puzzle_print(puzzle):
    for list_of_list in puzzle:
        print (''.join(str(num) for num in list_of_list))
