class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #return True if sorted(s) == sorted(t) else False
        
        if len(s) != len(t):
            return False
        
        chars1 = dict()
        chars2 = dict()
        
        for i in range(len(s)):
            chars1[s[i]] = 1 + chars1.get(s[i], 0)
            chars2[t[i]] = 1 + chars2.get(t[i], 0)
        
        for c in chars1:
            if chars1.get(c) != chars2.get(c):
                return False
        
        return True