class Solution:
    cache = {}
    def uniquePaths(self, m: int, n: int) -> int:
        # Base cases
        if (m == n == 1): return 1
        if (m == 0 or n == 0): return 0
        
        # Cache check
        if (m,n) in self.cache:
            return self.cache[(m,n)]
        
        # Novel value, how many paths from down tile and right tile
        self.cache[(m,n)] = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        
        # Return novel value
        return self.cache[(m,n)]
        