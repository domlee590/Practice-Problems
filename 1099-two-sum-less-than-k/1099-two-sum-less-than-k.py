class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = -1
        
        while l < r:
            cur = nums[l] + nums[r]
            if cur < k:
                res = max(res, cur)
                l += 1
            else:
                r -= 1
        
        return res