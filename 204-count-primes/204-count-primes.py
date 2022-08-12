class Solution:
    def countPrimes(self, n: int) -> int:
        # Sieve of Eratosthenes
        # Starting at 2, cross out (make false) multiples of largest uncrossed number
        
        if n == 0 or n == 1:
            return 0
        
        # Track primes
        primes = [True for _ in range(n)]
        
        # 0 and 1 are not prime
        primes[0] = False
        primes[1] = False
        
        # Only need to do numbers who can make composites < n
        num = 2
        while (num * num) < n:
            # if uncrossed, keep making new composites
            if primes[num]:
                composite = num * 2
                while composite < n:
                    primes[composite] = False
                    composite += num
                   
            num += 1
                
        # Start prime count at 2
        count = 0
        for num in primes:
            if num == True:
                count += 1
        
        return count