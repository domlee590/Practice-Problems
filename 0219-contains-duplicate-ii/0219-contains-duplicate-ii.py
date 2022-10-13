class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if len(nums) < 2:
            return False
        
        L = 0
        R = 1
        seen = collections.defaultdict(int)
        seen[nums[L]] += 1
        
        while R < len(nums):
            print(R)
            
            if abs(R - L) > k:
                seen[nums[L]] -= 1
                L += 1
            
            if seen[nums[R]] > 0:
                return True
            
            seen[nums[R]] += 1
            R += 1
        
        return False