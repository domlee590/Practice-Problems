class Solution:
    cache = {0:1}
    def climbStairs(self, n: int) -> int:
        # Check cache
        if n in self.cache:
            return self.cache[n]
        
        if n < 0: # Bad combination
            self.cache[n] = 0
            return self.cache[n]
        
        self.cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.cache[n]