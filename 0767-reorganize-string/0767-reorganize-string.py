class Solution:
    def reorganizeString(self, s: str) -> str:
        
        letters = Counter(s)
        
        heap = [(-v,k) for k,v in letters.items()]
        
        heapq.heapify(heap)
        res = []
        
        while(len(heap)>1):
            count1, letter1 = heapq.heappop(heap)
            count2, letter2 = heapq.heappop(heap)
            
            res.append(letter1)
            count1 += 1
            
            res.append(letter2)
            count2 += 1
            
            if count1:
                heapq.heappush(heap, (count1, letter1))
            if count2:
                heapq.heappush(heap, (count2, letter2))
                
        if heap:
            if heap[0][0] < -1:
                return ""
            res.append(heap[0][1])
                
        return "".join(res)
        