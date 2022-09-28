class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        numMap = collections.defaultdict(set)
        
        for i in range(len(nums)):
            numMap[nums[i]].add(i)
            
        for i in range(len(nums)):
            if nums[i] in numMap:
                for idx in numMap[nums[i]]:
                    if (abs(idx -i) <= k) and idx != i:
                        return True
        
        return False