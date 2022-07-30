class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # Define method for adding oranges to queue
        def addOrange(row, col):
            if (not (0 <= row < ROWS and 0 <= col < COLS) or 
               (row, col) in visited or
                grid[row][col] == 0):
                return
            
            visited.add((row, col))
            q.append((row, col))
        
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()
        oranges = 0
        
        # Get all rotten oranges in q, count total oranges
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] != 0:
                    if grid[row][col] == 2:
                        q.append((row, col))
                        visited.add((row, col))
                    oranges += 1
        
        if not oranges:
            return 0
        
        # BFS from rotten oranges
        minutes = -1
        while len(q) > 0:
            oranges -= len(q)
            for _ in range(len(q)): # Go by minute level
                row, col = q.popleft()
                
                addOrange(row + 1, col)
                addOrange(row - 1, col)
                addOrange(row, col + 1)
                addOrange(row, col - 1)
        
            minutes += 1
        
        return minutes if not oranges else -1
        