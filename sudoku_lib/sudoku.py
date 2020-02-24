import random
import copy


class Sudoku:

    region_sequence_defaults = {

        4: [[0, 0, 1, 1],
            [0, 0, 1, 1],
            [2, 2, 3, 3],
            [2, 2, 3, 3]],

        5: [[0, 0, 0, 1, 1],
            [0, 0, 3, 1, 1],
            [2, 3, 3, 3, 1],
            [2, 2, 3, 4, 4],
            [2, 2, 4, 4, 4]],

        6: [[0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [2, 2, 2, 3, 3, 3],
            [2, 2, 2, 3, 3, 3],
            [4, 4, 4, 5, 5, 5],
            [4, 4, 4, 5, 5, 5]],

        7: [[0, 0, 0, 1, 2, 2, 2],
            [0, 0, 1, 1, 1, 2, 2],
            [0, 0, 1, 1, 1, 2, 2],
            [3, 4, 4, 4, 4, 5, 5],
            [3, 3, 4, 4, 4, 5, 5],
            [3, 3, 6, 6, 6, 5, 5],
            [3, 3, 6, 6, 6, 6, 5]],

        8: [[0, 0, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 1, 1, 1],
            [2, 2, 2, 2, 3, 3, 3, 3],
            [2, 2, 2, 2, 3, 3, 3, 3],
            [4, 4, 4, 4, 5, 5, 5, 5],
            [4, 4, 4, 4, 5, 5, 5, 5],
            [6, 6, 6, 6, 7, 7, 7, 7],
            [6, 6, 6, 6, 7, 7, 7, 7]],

        9: [[0, 0, 0, 1, 1, 1, 2, 2, 2],
            [0, 0, 0, 1, 1, 1, 2, 2, 2],
            [0, 0, 0, 1, 1, 1, 2, 2, 2],
            [3, 3, 3, 4, 4, 4, 5, 5, 5],
            [3, 3, 3, 4, 4, 4, 5, 5, 5],
            [3, 3, 3, 4, 4, 4, 5, 5, 5],
            [6, 6, 6, 7, 7, 7, 8, 8, 8],
            [6, 6, 6, 7, 7, 7, 8, 8, 8],
            [6, 6, 6, 7, 7, 7, 8, 8, 8]]
    }

    def __init__(self, type='N', size=9):

        self.type = type
        self.size = size
        self.sudoku_complete = []
        self.sudoku = []
        self.region_sequence = self.region_sequence_defaults[size]

    def is_in_row(self, sudoku, num, row):
        return num in sudoku[row]

    def is_in_column(self, sudoku, num, col):
        for row in range(len(sudoku)):
            if num == sudoku[row][col]:
                return True
        return False

    def is_in_region(self, sudoku, num, reg):
        regional = self.row_to_region(sudoku)
        return num in regional[reg]

    def is_valid(self, sudoku, num, row, col):
        is_valid_move = not self.is_in_row(sudoku, num, row) and \
            not self.is_in_column(sudoku, num, col) and \
            not self.is_in_region(sudoku, num, self.region_sequence[row][col]) and \
            not self.is_cell_full(sudoku, row, col)

        return is_valid_move

    def is_cell_full(self, sudoku, row, col):
        return sudoku[row][col] is not None

    def print_sudoku(self, sudoku):
        size = self.size
        sdkstr = f" {(size*4-1)*'-'}" + '\n'
        reg_sq = self.region_sequence

        for i in range(size):
            row = ""
            for j in range(size):

                if j == 0:
                    sdkstr += '|'

                n = sudoku[i][j]

                if n == None:
                    n = ' '

                sdkstr += f" {str(n)} "

                if j != size-1:
                    sdkstr += '|' if reg_sq[i][j] != reg_sq[i][j+1] else ' '
                else:
                    sdkstr += '|'

                if j < size-1 and j == 0:
                    row += '|'

                row += "---" if i < size - \
                    1 and reg_sq[i][j] != reg_sq[i+1][j] else "   "

                if j < size-1:
                    row += '|' if reg_sq[i][j] != reg_sq[i][j +
                                                            1] and row[len(row)-1] != '-' else ' '
                else:
                    row += '|'

            sdkstr += '\n' + row + '\n' if i != size - \
                1 else '\n' + f" {(size*4-1)*'-'}"

        print(sdkstr)
        return sdkstr

    def count_number(self, sudoku, num):
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if sudoku[i][j] == num:
                    count += 1
        return count

    def row_to_region(self, sudoku):

        regional = [[] for i in range(self.size)]

        for i in range(self.size):
            for j in range(self.size):
                regional[self.region_sequence[i][j]].append(sudoku[i][j])

        return regional

    def generate_full(self):

        size = self.size
        attempt = 0
        num = 1
        self.sudoku_complete = [
            [None for i in range(size)] for j in range(size)]
        temp = [copy.deepcopy(self.sudoku_complete)]

        while num <= size:
            for row in range(size):

                valid_cells = [col for col in range(
                    size) if self.is_valid(self.sudoku_complete, num, row, col)]

                if len(valid_cells) == 0:
                    self.sudoku_complete = copy.deepcopy(temp[num-1])
                    break

                col = random.choice(valid_cells)
                self.sudoku_complete[row][col] = num

            attempt += 1

            if attempt == size*3:
                num -= 1
                self.sudoku_complete = copy.deepcopy(temp[num-1])
                temp.pop()
            elif attempt == size*5:
                self.generate_full()

            if self.count_number(self.sudoku_complete, num) == size:
                temp.append(copy.deepcopy(self.sudoku_complete))
                num += 1

    def finalize(self):

        s = self.size
        sudoku = copy.deepcopy(self.sudoku_complete)
        num = random.randint(s*(s-4), s*(s-2))
        count = 0

        while True:
            row = random.randint(0, s-1)
            col = random.randint(0, s-1)
            if self.is_cell_full(self.sudoku_complete, row, col):
                sudoku[row][col] = None
                count += 1
            if count == num:
                break

        self.sudoku = sudoku
        if self.backtrack()[0] == 1:
            return
        else:
            self.finalize()

    def backtrack(self):

        size = self.size
        sudoku = copy.deepcopy(self.sudoku)
        full_sudoku = None

        empty_cells = [[i, j, 0] for i in range(size) for j in range(
            size) if not self.is_cell_full(sudoku, i, j)]

        if len(empty_cells) == 0:
            return -1

        solution_count = 0

        position = 0
        first_loop = False
        while True:

            row = empty_cells[position][0]
            col = empty_cells[position][1]
            num = empty_cells[position][2]
            num += 1

            if sudoku[row][col] != None:
                sudoku[row][col] = None

            if num <= size:
                empty_cells[position][2] = num

                if self.is_valid(sudoku, num, row, col):
                    position += 1
                    sudoku[row][col] = num

            else:
                empty_cells[position][2] = 0
                position -= 1

            if position == len(empty_cells):
                solution_count += 1
                full_sudoku = copy.deepcopy(sudoku)

                position -= 1
                empty_cells[position][2] = 0
                position -= 1

            if empty_cells[0][2] == 0 and not first_loop:
                if solution_count == 1:
                    self.sudoku = sudoku
                break

        return solution_count, full_sudoku
