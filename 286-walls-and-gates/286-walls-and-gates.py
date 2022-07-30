class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:

        INF = 2147483647
        ROWS, COLS = len(rooms), len(rooms[0])
        q = collections.deque()
        visited = set()
        
        def addRoom(row, col):
            if (not (0 <= row < ROWS and 0 <= col < COLS) or 
               (row, col) in visited or
                rooms[row][col] == -1):
                return
            
            visited.add((row, col))
            q.append((row, col))
        
        # Add gates to queue's first level
        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] == 0:
                    q.append((row, col))
                    visited.add((row, col))
        
        distance = 0
        while len(q) > 0:
            lvlSize = len(q)
            for _ in range(lvlSize):
                row, col = q.popleft()
                rooms[row][col] = distance
                
                addRoom(row + 1, col)
                addRoom(row - 1, col)
                addRoom(row, col + 1)
                addRoom(row, col - 1)
                
            distance += 1