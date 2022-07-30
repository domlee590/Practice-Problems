class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Iterate through grid
        # Explore when encounter 1, change to -1 to mark visited, increment count
        
        islands = 0
        for row in range(len(grid)): # Rows
            for col in range(len(grid[0])): # Cols
                # Skip all 0's and -1's
                if grid[row][col] == "1":
                    self.dfs(grid, row, col)
                    islands += 1
        
        return islands
        
    def dfs(self, grid, row, col):
        # Mark as visited
        grid[row][col] = "-1"
        
        # Explore adjacent land (rows)
        if (row + 1 < len(grid) and grid[row + 1][col] == '1'):
            self.dfs(grid, row + 1, col)
        if (row - 1 >= 0 and grid[row - 1][col] == '1'):
            self.dfs(grid, row - 1, col)
            
        # Explore adjacent land (cols)
        if (col + 1 < len(grid[0]) and grid[row][col + 1] == '1'):
            self.dfs(grid, row, col + 1)
        if (col - 1 >= 0 and grid[row][col - 1] == '1'):
            self.dfs(grid, row, col - 1)