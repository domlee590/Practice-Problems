class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.split()
        res = ""
        
        for word in s:
            for i in range(len(word) - 1, -1 ,-1):
                res += word[i]
            res += " "
        
        return res[:len(res) - 1]