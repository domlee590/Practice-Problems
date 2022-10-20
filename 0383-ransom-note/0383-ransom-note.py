class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ransom = Counter(ransomNote)
        mag = Counter(magazine)
        
        for letter, count in ransom.items():
            if letter not in mag or mag[letter] < count:
                return False
        
        return True