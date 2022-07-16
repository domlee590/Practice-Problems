class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            lNum = nums[l] ** 2
            rNum = nums[r] ** 2
            
            if lNum >= rNum:
                res.append(lNum)
                l += 1
            else:
                res.append(rNum)
                r -= 1
        
        return res[::-1]