class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numMap = dict()
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in numMap:
                return [numMap[comp], i]
            else:
                numMap[nums[i]] = i
            
            
        