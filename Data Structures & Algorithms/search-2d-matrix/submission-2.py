class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        n = len(matrix[0])
        while r < len(matrix) and target > matrix[r][n - 1]:
            r+=1
        if r == len(matrix):
            return False
        for i in range(n):
            if matrix[r][i] == target:
                return True
        return False

        