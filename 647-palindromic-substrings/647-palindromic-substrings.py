class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        # Odd length palindromes
        # For each char
        for i in range(len(s)):
            l = r = i
            # Expand outward from single char, checking if still palindrome
            while (l >= 0) and (r < len(s)) and s[l] == s[r]:
                count += 1
                l -=1 
                r += 1
        
            # Even length palindromes
            # For each pair of characters
            l, r = i, i + 1
            while (l >= 0) and (r < len(s)) and s[l] == s[r]:
                count += 1
                l -=1 
                r += 1
                
        return count