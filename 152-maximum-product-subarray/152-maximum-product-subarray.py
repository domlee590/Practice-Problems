class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
            
            oldMax = curMax
            curMax = max(n, n * curMax, n * curMin)
            curMin = min(n, n * oldMax, n * curMin)
            
            res = max(res, curMax)
        
        return res