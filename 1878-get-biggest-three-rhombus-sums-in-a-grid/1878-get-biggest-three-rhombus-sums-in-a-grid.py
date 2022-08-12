class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        def getSum(l, r, t, b):
            locsum = 0
            col1 = col2 = (l+r)//2
            expand = True
            
            for row in range(t, b + 1):
                if col1 == col2:
                    locsum += grid[row][col1]
                else:
                    locsum += grid[row][col1] + grid[row][col2]
                
                # If a border has been reached
                if col1 == l or col2 == r:
                    expand = False
                    
                # Expand
                if expand:
                    col1 -= 1
                    col2 += 1
                else:
                    col1 += 1
                    col2 -= 1
            
            return locsum
        
        # M rows and N columns
        M, N = len(grid), len(grid[0])
        q = []
        
        # Fix the top of the rhombus.
        for t in range(M):
            for j in range(N):
                # Edge pointers start at current col
                l = r = j
                # Bottom pointer start at current row (top)
                b = t
                while l >= 0 and r < N and b < M:
                    # Get current sum funciton, left right top bottom
                    cursum = getSum(l, r, t, b)
                    l -= 1
                    r += 1
                    b += 2 # Bottom increases by 2
                    
                    if len(q) < 3:
                        if cursum not in q:
                            heapq.heappush(q, cursum)
                    else:
                        if cursum not in q and cursum > q[0]:
                            heapq.heappop(q)
                            heapq.heappush(q, cursum)
        
        q.sort()
        return q[::-1]
            