class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col, i):
            if i == len(word):
                return True
            if(row >= ROWS or col >= COLS or row < 0 or col < 0 or 
                board[row][col] != word[i] or (row, col) in visited):
                return False

            visited.add((row, col))
            found= (dfs(row+1, col, i+1) or 
                    dfs(row, col+1, i+1) or 
                    dfs(row-1, col, i+1) or 
                    dfs(row, col-1, i+1))
            visited.remove((row, col))

            return found

        visited = set()
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0): return True

        return False