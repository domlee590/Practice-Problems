class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums)
        return nums
    
    def mergeSort(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]
            
            # Call recursively on both halves
            self.mergeSort(left)
            self.mergeSort(right)
            
            L = R = cur = 0
            
            while L < len(left) and R < len(right):
                if left[L] < right[R]:
                    nums[cur] = left[L]
                    L += 1
                else:
                    nums[cur] = right[R]
                    R += 1
                cur += 1
            
            while L < len(left):
                nums[cur] = left[L]
                L += 1
                cur += 1
            
            while R < len(right):
                nums[cur] = right[R]
                R += 1
                cur += 1