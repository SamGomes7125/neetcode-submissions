class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Area = 0
        
        def dfs(row, col):
            if row < 0 or row >= len(grid):
                return 0
            if col < 0 or col >= len(grid[0]):
                return 0
            if grid[row][col] == 0:
                return 0
            else:
                grid[row][col] = 0
                A = 1
                A += dfs(row + 1, col)
                A += dfs(row - 1, col)
                A += dfs(row, col + 1)
                A += dfs(row, col - 1)
                return A
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    current_area = dfs(row, col)
                    Area = max(Area, current_area)                                 
        return Area