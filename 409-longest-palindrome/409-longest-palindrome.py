class Solution:
    def longestPalindrome(self, s: str) -> int:
        #Need to have multiple of 2 of a letter to form palindrome with
        #How much length a letter adds is floor(# of letter / 2)
        from collections import defaultdict
        
        chars = defaultdict(int)
        pal = 0
        
        for char in s:
            chars[char] += 1
        
        for count in chars.values():
            pal += (count // 2) * 2
            #Even length, all pairs, and can add centre unique
            if(pal % 2 == 0 and count % 2 == 1):
                pal += 1
        
        return pal