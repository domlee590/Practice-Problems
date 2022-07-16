class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        
        lSum = 0
        for i, n in enumerate(nums):
            rSum = total - lSum - n
            if lSum == rSum:
                return i
            lSum += n
        
        return -1