class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        
        lst = [-i for i in nums]
        
        heapNums = heapq.heapify(lst)
        
        for i in range(k):
            k = heapq.heappop(lst)
            
        return -k
        
        
        