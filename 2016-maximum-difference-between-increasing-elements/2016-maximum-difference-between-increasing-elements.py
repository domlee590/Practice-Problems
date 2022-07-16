class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        maxDiff = -1
        smallest = nums[0]
        
        for i in range(1, len(nums)):
            maxDiff = max(maxDiff, nums[i] - smallest)
            smallest = min(smallest, nums[i])
            
        return maxDiff if maxDiff > 0 else -1