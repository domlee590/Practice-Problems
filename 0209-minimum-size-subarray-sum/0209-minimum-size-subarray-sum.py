class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        minLen = len(nums) + 1
        curSum = 0
        L = R = 0
        
        while R < len(nums):
            curSum += nums[R]
            R += 1
            
            while curSum >= target:
                curSum -= nums[L]
                L += 1
                minLen = min(minLen, R - L + 1)
        
        return minLen if minLen < len(nums) + 1 else 0