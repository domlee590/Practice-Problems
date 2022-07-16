class Solution:
    def uniqueLetterString(self, s: str) -> int:
        occurances = [[-1, -1] for i in range(26)]
        
        current = 0
        total = 0
        for i in range(len(s)):
            
            letter = ord(s[i]) - 65
            
            secondLast, last = occurances[letter]
            
            #All strings without letter increase count by 1
            add = i - last
            
            #All strings with letter decrease count by 1
            remove = last - secondLast
            
            occurances[letter] = [last, i]
            
            current += add - remove
            total += current
        
        return total