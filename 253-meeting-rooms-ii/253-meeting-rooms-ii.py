class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meetings = sorted(intervals, key=lambda x: x[0])
        rooms = 1
        earlyEnd = []
        heapq.heappush(earlyEnd, meetings[0][1])

        for meeting in meetings[1:]:
            if meeting[0] < earlyEnd[0]: #meetings conflict
                rooms += 1
                heapq.heappush(earlyEnd, meeting[1]) #keep smallest end on top
            else: #meetings don't conflict
                #can use room that ended first. remove that endtime and add the new one for the room
                heapq.heappop(earlyEnd)
                heapq.heappush(earlyEnd, meeting[1])

        return rooms
