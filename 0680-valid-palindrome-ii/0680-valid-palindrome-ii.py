class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        L, R = 0, len(s) - 1

        while L < R:
            if s[L] != s[R]:
                if self.check(s[L + 1:R + 1]):
                    L += 1
                    continue
                elif self.check(s[L:R]):
                    R -= 1
                    continue
                else:
                    return False

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