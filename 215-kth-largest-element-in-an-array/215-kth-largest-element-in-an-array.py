from heapq import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        minheap = []
        
        for num in nums:
            if len(minheap) < k:
                heappush(minheap, num)
            else:
                if num > minheap[0]:
                    heappop(minheap)
                    heappush(minheap, num)
        
        return minheap[0]