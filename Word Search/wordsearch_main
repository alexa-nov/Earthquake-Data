from wordsearch_funcs import *

def main():
    puzzle_str = input()
    words_str = input()
    puzzle = format_rows(puzzle_str)
    words = format_words(words_str)
    ford = forward(puzzle, words)
    back = backward(puzzle_str, words)
    down = downward(puzzle, words)
    up = upward(puzzle, words)
    diag = diagonal(puzzle, words)
    
    print("Puzzle:")
    print('')
    puzzle_print(puzzle)
    print('')
    words_found = []
    
    for word in words:
        for i in range(len(ford)):
            if word in ford[i]:
                words_found.append(word)
                print(ford[i][0]+': '+ford[i][1], "row:", ford[i][2], "column:", ford[i][3])
        for i in range(len(back)):
            if word in back[i]:
                words_found.append(word)
                print(back[i][0]+': '+back[i][1], "row:", back[i][2], "column:", back[i][3])
        for i in range(len(down)):
            if word in down[i]:
                words_found.append(word)
                print(down[i][0]+': '+down[i][1], "row:", down[i][2], "column:", down[i][3])
        for i in range(len(up)):
            if word in up[i]:
                words_found.append(word)
                print(up[i][0]+': '+up[i][1], "row:", up[i][2], "column:", up[i][3])
        for i in range(len(diag)):
            if word in diag[i]:
                words_found.append(word)
                print(diag[i][0]+': '+diag[i][1], "row:", diag[i][2], "column:", diag[i][3])
        if word not in words_found:
            print(word+':',"word not found")

if __name__ == '__main__':
    main()

