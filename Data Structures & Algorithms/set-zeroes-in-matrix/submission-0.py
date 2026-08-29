class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = {}
        cols = {}
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    if r not in rows:
                        rows[r] = 1
                    if c not in cols:
                        cols[c] = 1                   
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if c in cols or r in rows:
                    matrix[r][c] = 0
      
        
        