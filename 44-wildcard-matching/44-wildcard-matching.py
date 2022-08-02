class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Fill an mxn matrix, m = len(s) + 1, n = len(p) + 1
        # Values will be booleans representing if p[0:i] generates s[0,j]
        ROWS, COLS = len(s) + 1, len(p) + 1
        generates = [ [None for _ in range(COLS)] for _ in range(ROWS) ]
        
        # Initialize matrix base cases
        # (0,0) will always be true, empty pattern derives empty string
        generates[0][0] = True
        
        for i in range(1, COLS):
            if p[i-1] == "*":
                generates[0][i] = generates[0][i - 1]
        
        
        for i in range(1, ROWS):
            for j in range(1, COLS):
                if s[i-1] == p[j-1] or p[j-1] == "?":
                    generates[i][j] = generates[i-1][j-1] #Current position guaranteed match, check previous
                if p[j-1] == "*":
                    # Can use empty string as *, so check if current string matches pattern up to *
                    # OR can use current char as *, so check if previous substring is valid
                    generates[i][j] = generates[i][j-1] or generates[i-1][j] or generates[i-1][j-1] 
    
        # Return if full string matches full patter
        return generates[ROWS-1][COLS-1]
        