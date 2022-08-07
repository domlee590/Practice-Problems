class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        
        for i in range(len(s)):
            # Odd length substrings
            pal = self.getLongest(s, i, i)
            if len(pal) > len(longest):
                longest = pal
            
            pal = self.getLongest(s, i, i + 1)
            if len(pal) > len(longest):
                longest = pal
        
        return longest
    
    # Perform expansion outward and get longest valid substring
    def getLongest(self, s, l, r):
        localLongest = ""
        while (l >= 0) and (r < len(s)) and (s[l] == s[r]):
                if (r - l + 1) > len(localLongest):
                    localLongest = s[l:r+1]
                l -= 1
                r += 1
        
        return localLongest