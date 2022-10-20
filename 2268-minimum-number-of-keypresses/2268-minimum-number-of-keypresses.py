class Solution:
    def minimumKeypresses(self, s: str) -> int:
        
        letters = Counter(s)
        total = 0
        
        letter = 0
        for k,v in sorted(letters.items(), key = lambda item: -item[1]):
            if letter < 9:
                total += 1 * v
            elif letter < 18:
                total += 2 * v
            else:
                total += 3 * v
            
            letter += 1
        
        return total