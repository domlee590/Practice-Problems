class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        for i in range(len(s)):
            # Odd length palindromes
            # For each char
            count += self.countPal(s, i, i)
        
            # Even length palindromes
            # For each pair of characters
            count += self.countPal(s, i, i+1)
            
        return count
    
    # Expand outward, checking if still palindrome
    def countPal(self, s, l, r):
        localCount = 0
        while (l >= 0) and (r < len(s)) and s[l] == s[r]:
            localCount += 1
            l -=1 
            r += 1

        return localCount