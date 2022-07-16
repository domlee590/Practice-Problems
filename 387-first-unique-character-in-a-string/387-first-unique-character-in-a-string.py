class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        dictionary = {}
        
        for i in range(len(s)):
            if s[i] in dictionary:
                dictionary[s[i]] += 1
            else:
                dictionary[s[i]] = 1
        
        for i in range(len(s)):
            if dictionary[s[i]] > 1:
                continue
            else:
                return i
                
        return -1