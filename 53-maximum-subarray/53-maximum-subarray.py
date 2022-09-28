class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        
        for n in nums:
            curSum = max(curSum, 0) # Discard current subarray if does not contribute positively
            curSum += n
            maxSum = max(maxSum, curSum) # Update maximum subarray when necessary
            
        return maxSum