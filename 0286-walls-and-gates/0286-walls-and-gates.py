class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        
        def addRoom(row, col):
            if (row >= 0 and col >= 0 and
                row < ROWS and col < COLS and
                rooms[row][col] != -1 and
                rooms[row][col] != 0 and
                (row, col) not in visited):
                
                q.append((row, col))
                visited.add((row, col))
        
        ROWS, COLS = len(rooms), len(rooms[0])
        q = collections.deque()
        visited = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        
        # BFS from each gate
        distance = 0
        while len(q) > 0:
            levelSize = len(q)
            for _ in range(levelSize):
                row, col = q.popleft()
                
                if (rooms[row][col] != -1 and 
                    rooms[row][col] != 0):
                    rooms[row][col] = distance
                
                addRoom(row - 1, col)
                addRoom(row + 1, col)
                addRoom(row, col + 1)
                addRoom(row, col - 1)
                
            distance += 1
        
        return
        