class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptS = ptT = 0
        
        if len(t) < len(s):
            return False
        
        while ptS < len(s):
            if ptT > len(t) - 1:
                return False
            
            if s[ptS] == t[ptT]:
                ptS += 1
            
            ptT += 1
        
        return True
            