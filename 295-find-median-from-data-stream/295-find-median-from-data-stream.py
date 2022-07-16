class MedianFinder:

    def __init__(self):
        #two heaps, large & small, min & max
        #heap size only differs by 1
        self.small = []
        self.large = []
        
    def addNum(self, num: int) -> None:
        #default push to small, which is max heap so *-1
        heapq.heappush(self.small, -1 * num)
        
        #ensure every element in small is <= large's
        if (self.small and self.large and 
            (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        #ensure sizes are within differ range
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return ((-1* self.small[0]) + self.large[0]) / 2