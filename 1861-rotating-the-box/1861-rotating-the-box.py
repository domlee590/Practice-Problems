class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # Constants
        ROWS, COLS = len(box), len(box[0])
        
        # Falling logic
        for r in range(ROWS):
            # Start column scan from "bottom" (R->L)
            for c in range(COLS - 1, -1 , -1):
                # If a rock is found
                if box[r][c] == "#":
                    # Scan L->R for next obstacle
                    obs = c + 1
                    while obs < COLS and box[r][obs] == ".":
                        obs += 1
                    
                    # Mark current cell as empty and cell left of obstacle as rock
                    # If the rock doesn't move, nothing changes
                    box[r][c] = "."
                    box[r][obs - 1] = "#"
        
        # Rotation
        rotBox = [[None for _ in range(ROWS)] for _ in range(COLS)]
        curCol = ROWS - 1
        for r in range(ROWS):
            for c in range(COLS):
                rotBox[c][curCol] = box[r][c]
            curCol -= 1
        
        return rotBox