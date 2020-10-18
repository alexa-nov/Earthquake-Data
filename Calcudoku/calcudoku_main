from calcudoku_funcs import *

def main():
    cages = get_cages()
    puzzle = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]

    #Initialize Values
    current_index = 0
    checks = 0
    backtracks = 0
    
    while current_index < 25:
        current_value = puzzle[current_index // 5][current_index % 5]
        is_valid = False
        for new_value in range(current_value + 1, 6):
            puzzle[current_index // 5][current_index % 5] += 1
            checks += 1
            if check_valid(puzzle, cages) == True:
                is_valid = True
                break
        #increment and move forward
        if is_valid == True:
            current_index += 1
        #set to 0 and move backwards
        else:
            puzzle[current_index // 5][current_index % 5] = 0
            current_index -= 1
            backtracks +=1

    #Output to Screen
    print("---Solution---")
    print(" ")
    puzzle_print(puzzle)
    print(" ")
    print("checks: %d backtracks: %d" %(checks, backtracks))

if __name__ == '__main__':
    main()

