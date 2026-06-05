class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        squares = set()
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == '.':
                    continue
                else:
                    value = board[r][c]
                    row_key = (r, value)
                    if row_key in rows:
                        return False
                    else:
                        rows.add(row_key)
                    col_key = (c, value)
                    if col_key in cols:
                        return False
                    else:
                        cols.add(col_key)
                    square_key = (r//3, c//3, value)
                    if square_key in squares:
                        return False
                    else:
                        squares.add(square_key)
        return True
                


         


        