class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of all tasks. For efficiency will want
        # to always choose most common task (heap), and wait n intervals
        # until can use again (queue)
        
        taskCounts = Counter(tasks)
        maxheap = [-count for count in taskCounts.values()]
        heapq.heapify(maxheap)
        
        interval = 0
        queue = deque()
        while maxheap or queue:
            
            if maxheap:
                curTsk = heapq.heappop(maxheap)
                curTsk += 1 # Decrease occurences of this task by 1
                if curTsk != 0:
                    queue.append( (curTsk, interval + n) )
            
            if queue and queue[0][1] <= interval:
                newTsk = queue.popleft()[0]
                heapq.heappush(maxheap, newTsk)
            
            interval += 1
        
        return interval
            
            
            