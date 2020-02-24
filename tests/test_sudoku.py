import unittest
import sudoku_lib

from sudoku_lib import Sudoku
"use > python -m unittest tests.test_sudoku"

class TestBactracking(unittest.TestCase):
    
    def test_full_sudoku(self):
        s = Sudoku(size=4)
        sudoku =  [
            [1,3,2,4],
            [4,2,1,3],
            [2,4,3,1],
            [3,1,4,2]]
        s.sudoku = [
            [1,3,2,4],
            [4,2,1,3],
            [2,4,3,1],
            [3,1,4,2]]

        s.sudoku = s.backtrack()[1]
        self.assertEqual(sudoku, s.sudoku)
        
    def test_one_cell_empty(self):

        s = Sudoku(size=4)
        sudoku =  [
            [1,3,2,4],
            [4,2,1,3],
            [2,4,3,1],
            [3,1,4,2]]
        s.sudoku = [
            [1,3,2,4],
            [4,2,None,3],
            [2,4,3,1],
            [3,1,4,2]]
        

        s.sudoku = s.backtrack()[1]
        self.assertEqual(sudoku, s.sudoku)
        

if __name__ == '__main__':
    unittest.main()