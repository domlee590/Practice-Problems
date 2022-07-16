from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
    
        prefixes = defaultdict(int)
        prefixes[0] = 1 #beginning of array
        
        total = 0
        curSum = 0
        for n in nums:
            curSum += n
            
            #how many subarrays can we remove to get the target sum
            total += prefixes[curSum - k]
            
            prefixes[curSum] += 1
        
        return total