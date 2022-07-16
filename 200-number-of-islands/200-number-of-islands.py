class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0    
    
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    islands += 1
                    self.dfs(grid, i, j)
        
        return islands
    
    def dfs(self, grid, i, j):
            #Conditions not met for island
            if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or
                grid[i][j] != "1"):
                return
            
            #DEPTH, visit all adjacent spots recursively
            grid[i][j] = "-1" #mark as visited
            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i, j-1) 