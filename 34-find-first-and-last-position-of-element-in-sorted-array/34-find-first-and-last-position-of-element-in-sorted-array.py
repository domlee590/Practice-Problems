class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binSearch(lookLeft) -> int:
            l, r = 0, len(nums) - 1
            pos = -1
            
            while l <= r:
                m = (r+l) // 2
                
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    pos = m
                    if lookLeft:
                        r = m - 1
                    else: #search for right
                        l = m + 1
            
            return pos
        
        left = binSearch(True)
        right = binSearch(False)
        
        return [left, right]