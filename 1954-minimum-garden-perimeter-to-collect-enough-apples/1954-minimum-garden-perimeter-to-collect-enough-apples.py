class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        lo, hi = 1, 100000
        
        while lo < hi:
            m = (lo+hi)//2
            n = 2*m*(m+1)*(2*m+1)
            
            if n < neededApples: 
                lo = m+1
            else: 
                hi = m

        return 8*lo
        