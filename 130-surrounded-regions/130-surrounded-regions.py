class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        # Get Rows and Cols
        self.ROWS, self.COLS = len(board), len(board[0])
        
        # All O clusters connected to edges are safe. Explore them
        # First and last row
        for col in range(self.COLS):
            if board[0][col] == "O":
                self.dfs(board, 0, col)
            if board[self.ROWS-1][col] == "O":
                self.dfs(board, self.ROWS-1, col)
        # Left and right columns
        for row in range(self.ROWS):
            if board[row][0] == "O":
                self.dfs(board, row, 0)
            if board[row][self.COLS-1] == "O":
                self.dfs(board, row, self.COLS-1)
                
        # Flip unsafe O's
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'S':
                    board[row][col] = 'O'
        
    def dfs(self, board, row, col):
        # OOB check
        if not (0 <= row < self.ROWS and 0 <= col < self.COLS):
            return
        
        # Non-O check
        if (board[row][col] != 'O'):
            return
        
        # Mark safe
        board[row][col] = "S"
        
        # Explore adjacent tiles to mark clear
        self.dfs(board, row + 1, col)
        self.dfs(board, row - 1, col)
        self.dfs(board, row, col + 1)
        self.dfs(board, row, col - 1)