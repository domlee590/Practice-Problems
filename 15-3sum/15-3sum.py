class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            self.find(nums, -nums[i], i+1, ans)
        
        return ans
    
    def find(self, nums, targ, l, ans):
        r = len(nums) - 1
        
        while l < r:
            curSum = nums[l] + nums[r]
            if curSum == targ:
                ans.append([-targ, nums[l], nums[r]])
                l += 1
                r -= 1
                while l<r and l>0 and nums[l] == nums[l-1]:
                    l += 1
                while l<r and r<len(nums)-1 and nums[r] == nums[r+1]:
                    r -= 1
            
            elif curSum < targ:
                l += 1
            else:
                r -= 1
    