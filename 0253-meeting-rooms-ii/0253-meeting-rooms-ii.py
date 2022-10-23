class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[0])
        q = []
        heapq.heappush(q, intervals[0][1])
        rooms = 1
        
        for meeting in intervals[1:]:
            if meeting[0] < q[0]:
                rooms += 1
            else:
                heapq.heappop(q)
            heapq.heappush(q, meeting[1])
            
        return rooms