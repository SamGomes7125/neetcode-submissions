class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used = set()
        index = 0
        def recursion(row, column, index):
            if (row, column) in used:
                return False
            if row < 0 or row >= len(board):
                return False
            if column < 0 or column >= len(board[0]):
                return False
            if board[row][column] != word[index]:
                return False
            if index == len(word)-1:
                return True
            elif index < len(word):
                used.add((row, column))
                if recursion(row + 1, column, index + 1):
                    return True
                if recursion(row - 1, column, index + 1):
                    return True
                if recursion(row, column + 1, index + 1):
                    return True
                if recursion(row, column - 1, index + 1):
                    return True
                used.remove((row, column))
                return False
            
        for row in range(len(board)):
            for column in range(len(board[0])):
                if recursion(row, column, 0):
                    return True

        return False

        