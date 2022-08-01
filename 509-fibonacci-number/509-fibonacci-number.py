class Solution:
    
    # Create memoization hashmap
    cache = dict()
    
    def fib(self, n: int) -> int:
        # Check if value has been cached
        if n in self.cache:
            return self.cache[n]
        # Fibonacci base case
        if n == 0 or n == 1:
            return n
        # Cache novel value
        self.cache[n] = self.fib(n-1) + self.fib(n-2)
        # Return novel value
        return self.cache[n]
        