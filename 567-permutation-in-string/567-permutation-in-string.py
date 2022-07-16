class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        chars1 = [0 for _ in range(26)]
        chars2 = [0 for _ in range(26)]
        matches = 0
        
        for i in range(len(s1)):
            chars1[ord(s1[i]) - ord('a')] += 1
            chars2[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26):
            if chars2[i] == chars1[i]:
                matches += 1
        
        start = 0
        for end in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[end]) - ord('a')
            chars2[index] += 1
            if chars2[index] == chars1[index]: #now equal
                matches += 1
            elif chars2[index] == chars1[index] + 1: #too many
                matches -= 1
            
            index = ord(s2[start]) - ord('a')
            chars2[index] -= 1
            if chars2[index] == chars1[index]:
                matches += 1
            elif chars2[index] == chars1[index] - 1: #too few
                matches -= 1
            
            start += 1
        
        return False if matches != 26 else True