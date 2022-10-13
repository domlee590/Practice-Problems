class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        L = 0
        R = k - 1
        tot = 0
        res = 0
        
        for i in range(k):
            tot += arr[i]
        
        while R < len(arr):
            
            if (tot / k) >= threshold:
                res += 1
            
            if R == len(arr) - 1:
                break
            
            R += 1
            tot += arr[R]
            
            tot -= arr[L]
            L += 1
            
        return res