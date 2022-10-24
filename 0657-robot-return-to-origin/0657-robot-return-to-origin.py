class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        x, y = 0, 0
        
        for i in range(len(moves)):
            if moves[i] == "U":
                y += 1
            elif moves[i] == "D":
                y -= 1
            elif moves[i] == "L":
                x -= 1
            else:
                x += 1
                
        return True if (x, y) == (0, 0) else False