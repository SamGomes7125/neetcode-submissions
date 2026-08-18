class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def dfs(row, col):
            if row < 0 or row >= len(grid):
                return
            if col < 0 or col >= len(grid[0]):
                return
            if grid[row][col] == "0":
                return
            else:
                grid[row][col] = "0"
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)
                return
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1 
                    dfs(row, col)                                  
        return count
        