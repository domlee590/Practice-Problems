class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        
        rocks = [-i for i in stones]
        
        heapq.heapify(rocks)
        
        while len(rocks) > 1:
            bigStone = -1 * heapq.heappop(rocks)
            smallStone = -1 * heapq.heappop(rocks)
            
            if bigStone > smallStone:
                newStone = -1 * (bigStone - smallStone)
                heapq.heappush(rocks, newStone)
        
        if rocks:
            return -1 * heapq.heappop(rocks)
        
        return 0