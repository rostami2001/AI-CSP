from CSP.Solver import Solver
from States.StatesProblem import StatesProblem
from Sudoku.SudokuProblem import SudokuProblem
from CSP.Solver import Solver
from crossmathProblem import CrossMathProblem


grid = [
    [2, 0, 0, 3, 0, 0, 0, 0, 0],
    [8, 0, 4, 0, 6, 2, 0, 0, 3],
    [0, 1, 3, 8, 0, 0, 2, 0, 0],

    [0, 0, 0, 0, 2, 0, 3, 9, 0],
    [5, 0, 7, 0, 0, 0, 6, 2, 1],
    [0, 3, 2, 0, 0, 6, 0, 0, 0],

    [0, 2, 0, 0, 0, 9, 1, 4, 0],
    [6, 0, 1, 2, 5, 0, 8, 0, 9],
    [0, 0, 0, 0, 0, 1, 0, 0, 2]
]

grid1 = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],

    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],

    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]

grid2 = [
    [0, 0, 3, 0, 2, 0, 6, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],

    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 6, 7, 0, 8, 2, 0, 0],

    [0, 0, 2, 6, 0, 9, 5, 0, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 9],
    [0, 0, 5, 0, 1, 0, 3, 0, 0]
]


if __name__ == '__main__':
    sudoku = SudokuProblem(grid)
    s = Solver(sudoku)
    s.solve()
    sudoku.print_assignments()

    sudoku = SudokuProblem(grid1)
    s = Solver(sudoku)
    s.solve()
    sudoku.print_assignments()

    sudoku = SudokuProblem(grid2)
    s = Solver(sudoku, use_forward_check=True)
    s.solve()
    sudoku.print_assignments()

    states = StatesProblem()
    s = Solver(states, use_forward_check=True)
    s.solve()
    states.print_assignments()

    crossMath = CrossMathProblem()
    c = Solver(crossMath, use_forward_check=True)
    c.solve()
    crossMath.print_assignments()