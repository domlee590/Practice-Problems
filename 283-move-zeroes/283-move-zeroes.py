class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curNum = nxt = 0
        
        while curNum < len(nums):
            if nums[curNum] != 0:
                nums[nxt], nums[curNum] = nums[curNum], nums[nxt]
                nxt += 1
            curNum += 1
            