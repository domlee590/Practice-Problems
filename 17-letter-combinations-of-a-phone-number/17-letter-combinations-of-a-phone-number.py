class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        NUMSLETS = {2:["a","b","c"], 3:["d","e","f"],
                   4: ["g","h","i"], 5:["j","k","l"], 6:["m","n","o"],
                   7:["p","q","r","s"], 8:["t","u","v"], 9:["w","x","y","z"]}
        
        combinations = []
        
        def backtrack(i, string):
            if len(string) == len(digits):
                combinations.append(string)
                return
            # Loop over all chars mapped to digit at i
            for char in NUMSLETS[int(digits[i])]: 
                backtrack(i+1, string+char)
            
        backtrack(0, "")
        return combinations