class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0 for _ in range(len(temperatures))]
        
        for day in range(len(temperatures)):
            # while the top of the stack's temp is greater than current day
            while stack and temperatures[stack[-1]] < temperatures[day]:
                # pop the last day
                last = stack.pop()
                # this day's next highest temp is current, so put difference
                res[last] = day - last
                
            # today is not warmer
            stack.append(day)
                
        return res