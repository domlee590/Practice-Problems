class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 2:
            return True
        
        intervals.sort(key = lambda x: x[0])
        
        lastEnd = 0
        for meeting in intervals:
            if meeting[0] < lastEnd:
                return False
            lastEnd = meeting[1]
        
        return True