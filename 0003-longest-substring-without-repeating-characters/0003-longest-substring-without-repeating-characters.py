class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxLen = start = end = 0
        seen = set()
        
        while end < len(s):
            
            while s[end] in seen:
                seen.remove(s[start])
                start += 1
            
            seen.add(s[end])
            maxLen = max(maxLen, end - start + 1)
            end += 1
        
        return maxLen
        