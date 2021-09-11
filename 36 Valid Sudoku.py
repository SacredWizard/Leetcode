class Solution:
    def isValidSudoku(self, board):
        seen = set()
        return not any(x in seen or seen.add(x)
                       for i, row in enumerate(board)
                       for j, c in enumerate(row)
                       if c != '.'
                       for x in ((c, i), (j, c), (i // 3, j // 3, c)))

    def isValidSudokuOld(self, board):
        for i in range(3):
            for k in range(3):
                vals = list()
                for j in range(3):
                    for l in range(3):
                        try:
                            vals.append(int(board[3 * i + j][3 * k + l]))
                        except:
                            pass
                if len(set(vals)) != len(vals):
                    return False

        for i in range(9):
            vals = list()
            for j in range(9):
                try:
                    vals.append(int(board[i][j]))
                except:
                    pass
            if len(set(vals)) != len(vals):
                return False

        for i in range(9):
            vals = list()
            for j in range(9):
                try:
                    vals.append(int(board[j][i]))
                except:
                    pass
            if len(set(vals)) != len(vals):
                return False

        return True


if __name__ == "__main__":
    print(Solution().isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                                       , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                       , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                       , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                       , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                       , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                       , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                       , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                       , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
    print(Solution().isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."]
                                       , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                       , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                       , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                       , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                       , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                       , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                       , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                       , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
