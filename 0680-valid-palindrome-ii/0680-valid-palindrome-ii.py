class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        L, R = 0, len(s) - 1

        while L < R:
            if s[L] != s[R]:
                return (self.check(s[L + 1:R + 1]) or self.check(s[L:R]))

            L += 1
            R -= 1
        
        return True
    
    def check(self, s) -> bool:
            L, R = 0, len(s) - 1

            while L < R:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1

            return True