"""
This is just a past-time scribble and has nothing to do with machine learning.
The program solves a Sudoku using a recursive approach with back-tracking.
"""

import time
import copy

s = [[0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
     [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
     [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
     [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
     [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
     [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
     [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
     [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]  # 8

a = [[0, 6, 9, 0, 5, 0, 0, 0, 0],  # 0
     [7, 0, 0, 0, 0, 1, 0, 0, 0],  # 1
     [3, 0, 0, 0, 2, 0, 0, 0, 6],  # 2
     [0, 0, 4, 0, 0, 7, 0, 0, 2],  # 3
     [0, 0, 0, 2, 1, 0, 9, 0, 8],  # 4
     [0, 0, 0, 0, 0, 9, 5, 0, 0],  # 5
     [0, 0, 0, 1, 0, 0, 0, 6, 0],  # 6
     [6, 0, 0, 8, 0, 0, 7, 0, 5],  # 7
     [0, 4, 0, 0, 6, 0, 2, 0, 0]]  # 8

b = [[0, 0, 7, 0, 0, 0, 0, 0, 0],  # 0
     [2, 0, 0, 4, 0, 0, 7, 0, 8],  # 1
     [0, 1, 0, 0, 0, 3, 0, 0, 6],  # 2
     [0, 0, 0, 9, 0, 0, 0, 0, 2],  # 3
     [9, 5, 0, 1, 0, 0, 0, 4, 0],  # 4
     [0, 7, 0, 3, 5, 0, 0, 9, 0],  # 5
     [0, 8, 0, 0, 2, 0, 0, 0, 0],  # 6
     [0, 6, 0, 0, 0, 0, 0, 0, 0],  # 7
     [0, 0, 1, 7, 0, 0, 0, 3, 0]]  # 8

c = [[0, 0, 7, 8, 0, 0, 0, 0, 9],  # 0
     [4, 0, 1, 0, 0, 0, 5, 0, 2],  # 1
     [0, 0, 2, 0, 0, 6, 0, 7, 0],  # 2
     [0, 0, 3, 0, 6, 0, 4, 2, 0],  # 3
     [0, 0, 0, 5, 0, 0, 0, 0, 0],  # 4
     [0, 1, 0, 0, 0, 0, 0, 0, 8],  # 5
     [0, 9, 0, 7, 0, 0, 0, 0, 0],  # 6
     [3, 0, 0, 2, 5, 0, 0, 0, 0],  # 7
     [0, 0, 0, 0, 0, 3, 0, 0, 0]]  # 8


def sudoku(matrix, cal_num):
    cal_num[0] = cal_num[0] + 1

    for mRow in range(9):
        for mCol in range(9):
            num = matrix[mRow][mCol]
            if num == 0:
                valid_numbers_horizontal = [n for n in range(1, 10) if n not in matrix[mRow]]
                valid_numbers_vertical = [n for n in range(1, 10) if n not in [matrix[i][mCol] for i in range(9)]]
                valid_numbers_quadrant = [n for n in range(1, 10) if n not in get_quadrant_numbers(mCol, mRow, matrix)]
                valid_numbers = set(valid_numbers_horizontal) & set(valid_numbers_vertical) & set(valid_numbers_quadrant)

                if len(valid_numbers) == 0:
                    return None

                for vn in valid_numbers:
                    solution_matrix = copy.deepcopy(matrix)
                    solution_matrix[mRow][mCol] = vn

                    res = sudoku(solution_matrix, cal_num)
                    if res is not None:
                        return res

                return None

    return matrix


def pretty_print_matrix(matrix):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print "-" * 28
        row_str = ""
        for col in range(9):
            if col % 3 == 0 and col != 0:
                row_str = row_str + "| " + str(matrix[row][col]) + " "
            else:
                row_str = row_str + " " + str(matrix[row][col]) + " "
        print row_str




def get_quadrant_numbers(x, y, matrix):
    q_ver = (y / 3) * 3
    q_hor = (x / 3) * 3
    q_rows = matrix[q_ver:q_ver + 3]
    return list(set([item for sublist in [r[q_hor:q_hor + 3] for r in q_rows] for item in sublist if item != 0]))


for m in [a, b, c]:
    start_time = time.time()
    cal_num = [0]
    solution = sudoku(m, cal_num)
    pretty_print_matrix(solution)
    print cal_num[0], time.time() - start_time
