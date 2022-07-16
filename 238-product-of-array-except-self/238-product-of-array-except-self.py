class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1 for _ in range(len(nums))]
        
        prod = 1
        for i in range(len(nums)):
            out[i] = prod
            prod = prod * nums[i]
        
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * prod
            prod = prod * nums[i]
        
        return out