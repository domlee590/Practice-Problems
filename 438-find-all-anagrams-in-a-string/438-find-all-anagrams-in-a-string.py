class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        freqMapP, freqMapS = [0] * 26, [0] * 26
        anagrams = []
        
        for i in range(len(p)):
            freqMapP[ord(p[i]) - ord('a')] += 1

        for i in range(len(s)):
            # Remove left
            if i >= len(p):
                char = ord(s[i-len(p)]) - ord('a')
                freqMapS[char] -= 1
            
            # Add right
            char = ord(s[i]) - ord('a')
            freqMapS[char] += 1
            
            if freqMapP == freqMapS:
                anagrams.append(i - len(p) + 1)
        
        return anagrams
            
            