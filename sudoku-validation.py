
"""
As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.
If you need more details, you can find them here.

Your task is to write a program which:

reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
outputs Yes if the Sudoku is valid, and No otherwise.
Test your code using the data we've provided.
**Test data is stored separately.
"""

# A function that checks whether a list passed as an argument contains
# nine digits from '1' to '9'.
def checkset(digs):
    if digs.isdigit() and len(str(digs)) == 9:
        return sorted(list(digs)) == [str(x) for x in range(1, 10)]
    else:
        print("Sudoku must be all digits and 9x9 - found: ", digs)
        return False


# A list of rows representing the sudoku.
rows = []
filename = input("Enter the filename with the 9x9 Sudoku: ")
with open(filename) as file:
    for line in file:
        rows.append(line.rstrip())

ok = True

# Check if all rows are good.
for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break

# Check if all columns are good.
if ok:
    for c in range(9): #cols
        col_str = ''
        for r in range(9): #rows
            col_str += rows[r][c]
        #print("col_str is: ", col_str)
        if not checkset(col_str):
            ok = False
            break

# Check if all sub-squares (3x3) are good.
if ok:
    for i in range(0, 9, 3):  # big quare rows
        for j in range(0, 9, 3):  # column startings
            sub_box_string = ''
            for r in range(3):
                row = i + r
                row_string = ''
                for c in range(3):
                    col = j + c
                    row_string += rows[row][col]
                sub_box_string += row_string
            #check the sub_box
            print("sub_box_string is: ", sub_box_string, end=' ')
            if not checkset(sub_box_string):
                ok = False
                #break
                print("* BAD") #mark the sub-boxes that are bad, to check
            print()

# Print the final verdict.
if ok:
    print("Yes it's a valid Sudoku")
else:
    print("No it's not a valid Sudoku")
