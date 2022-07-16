class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cur = 0
        
        while cur < len(nums):
            if nums[cur] == len(nums):
                cur += 1
                continue
            target = nums[cur]
            if nums[cur] != nums[target]:
                nums[cur], nums[target] = nums[target], nums[cur]
            else:
                cur += 1
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        
        return len(nums)