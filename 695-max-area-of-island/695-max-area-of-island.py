class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Iterate through grid
        # Explore when encounter 1, change to -1 to mark visited, increment count
        
        biggest = 0
        for row in range(len(grid)): # Rows
            for col in range(len(grid[0])): # Cols
                # Skip all 0's and -1's
                if grid[row][col] == 1:
                    size = self.dfs(grid, row, col)
                    biggest = max(biggest, size)
        
        return biggest
        
    def dfs(self, grid, row, col):
        # Mark as visited
        grid[row][col] = -1
        
        # Size for call starts at current tile
        size = 1
        
        # Accumulate size by adding each visited tile through callstack
        # Explore adjacent land (rows)
        if (row + 1 < len(grid) and grid[row + 1][col] == 1):
            size += self.dfs(grid, row + 1, col)
        if (row - 1 >= 0 and grid[row - 1][col] == 1):
            size += self.dfs(grid, row - 1, col)
            
        # Explore adjacent land (cols)
        if (col + 1 < len(grid[0]) and grid[row][col + 1] == 1):
            size += self.dfs(grid, row, col + 1)
        if (col - 1 >= 0 and grid[row][col - 1] == 1):
            size += self.dfs(grid, row, col - 1)
        
        return size