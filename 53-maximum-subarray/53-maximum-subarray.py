class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSub = curSub = nums[0]
        
        for num in nums[1:]:
            #Keep the subarray if next number keeps cursub bigger than itself
            curSub = max(num, curSub + num)
            maxSub = max(curSub, maxSub)
        
        return maxSub