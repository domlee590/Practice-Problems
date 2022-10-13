class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        L = 0
        R = k - 2
        tot = 0
        res = 0
        
        for i in range(k - 1):
            tot += arr[i]
        
        while R < len(arr) - 1:
            R += 1
            tot += arr[R]
            
            if (tot / k) >= threshold:
                res += 1
            
            tot -= arr[L]
            L += 1
            
        return res