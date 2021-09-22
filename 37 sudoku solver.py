class Solution:

    def nextCell(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    return i, j
        return -1, -1

    def isValidSudoku(self, board):
        seen = set()
        return not any(x in seen or seen.add(x)
                       for i, row in enumerate(board)
                       for j, c in enumerate(row)
                       if c != "."
                       for x in ((c, i, j), (i // 3, j // 3, c)))

    def isValid(self, board, i, j, e):
        row_valid = not any(e == x for x in board[i])
        if row_valid:
            col_valid = not any(e == board[x][j] for x in range(9))
            if col_valid:
                sec_x, sec_y = 3 * (i // 3), 3 * (j // 3)
                return not any(e == board[x][y] for x in range(sec_x, sec_x + 3) for y in range(sec_y, sec_y + 3))
            return False
        return False

    def solveSudoku(self, board):
        i, j = self.nextCell(board)
        if i == -1:
            return True
        for e in range(1, 10):
            if self.isValid(board, i, j, str(e)):
                board[i][j] = str(e)
                if self.solveSudoku(board):
                    return True
            board[i][j] = "."
        return False


if __name__ == "__main__":
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    Solution().solveSudoku(board)
    print(board)
