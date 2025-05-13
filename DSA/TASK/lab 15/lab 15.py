# task 1

def solve_n_queens(n):
    def is_safe(row, col, diagonals, anti_diagonals, cols):
        return col not in cols and (row - col) not in diagonals and (row + col) not in anti_diagonals

    def backtrack(row, diagonals, anti_diagonals, cols, board):
        if row == n:
            result.append(["".join(r) for r in board])
            return
        for col in range(n):
            if not is_safe(row, col, diagonals, anti_diagonals, cols):
                continue
            board[row][col] = 'Q'
            diagonals.add(row - col)
            anti_diagonals.add(row + col)
            cols.add(col)

            backtrack(row + 1, diagonals, anti_diagonals, cols, board)

            board[row][col] = '.'
            diagonals.remove(row - col)
            anti_diagonals.remove(row + col)
            cols.remove(col)

    result = []
    empty_board = [["."] * n for _ in range(n)]
    backtrack(0, set(), set(), set(), empty_board)
    return result

# Example
from pprint import pprint
pprint(solve_n_queens(4))


# task 2

def permute(s):
    def backtrack(start):
        if start == len(chars):
            result.append("".join(chars))
            return
        seen = set()
        for i in range(start, len(chars)):
            if chars[i] in seen:
                continue  # Avoid duplicates
            seen.add(chars[i])
            chars[start], chars[i] = chars[i], chars[start]
            backtrack(start + 1)
            chars[start], chars[i] = chars[i], chars[start]

    chars = list(s)
    result = []
    backtrack(0)
    return result

# Example
print(permute("ABC"))

# task 3

def solve_sudoku(board):
    def is_valid(row, col, num):
        box_index = (row // 3) * 3 + (col // 3)
        return (num not in rows[row] and
                num not in cols[col] and
                num not in boxes[box_index])

    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(i, j, num):
                            board[i][j] = num
                            rows[i].add(num)
                            cols[j].add(num)
                            boxes[(i // 3) * 3 + (j // 3)].add(num)

                            if backtrack():
                                return True

                            board[i][j] = 0
                            rows[i].remove(num)
                            cols[j].remove(num)
                            boxes[(i // 3) * 3 + (j // 3)].remove(num)
                    return False
        return True

    # Initialize sets for constraints
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                num = board[i][j]
                rows[i].add(num)
                cols[j].add(num)
                boxes[(i // 3) * 3 + (j // 3)].add(num)

    backtrack()
    return board

# Example (partially filled)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solved = solve_sudoku(sudoku_board)
from pprint import pprint
pprint(solved)

