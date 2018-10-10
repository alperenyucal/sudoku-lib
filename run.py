from sudoku import Sudoku

x = Sudoku(size=7)

"""x.box_sequence = [
    [0,0,0,1,1],
    [0,0,1,1,1],
    [2,2,2,3,3],
    [2,2,4,3,3],
    [4,4,4,4,3]]"""

x.generate()
x.finalize()
x.encode()
print(x.encoded_string)
x.print_sudoku(x.sudoku)
x.print_sudoku(x.finalized)

print(x.backtrack())
x.print_sudoku(x.finalized)