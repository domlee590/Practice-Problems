class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Backtracking approach
        
        subsets, current = [], []
        self.helper(0, nums, current, subsets)
        return subsets
        
    def helper(self, i, nums, current, subsets):
        if i == len(nums):
            subsets.append(current.copy())
            return
        
        current.append(nums[i])
        self.helper(i+1, nums, current, subsets)
        current.pop()
        
        self.helper(i+1, nums, current, subsets)