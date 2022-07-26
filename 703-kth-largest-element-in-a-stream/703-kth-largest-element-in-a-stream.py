from heapq import *

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = []
        self.k = k
        for val in nums:
            self.add(val)

    def add(self, val: int) -> int:
        
        if len(self.minheap) < self.k:
            heappush(self.minheap, val)
        else:
            if val > self.minheap[0]:
                heappop(self.minheap)
                heappush(self.minheap, val)
        
        return self.minheap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)