class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Create array of length n representing the cost to reach top
        # T[-1] is the "top", and can be reached in 0 steps
        T = [0 for _ in range(len(cost) + 1)]
        
        # Seed the base case, the last step must cost itself to reach top
        T[-2] = cost[-1]
        
        for i in range(len(T) - 3, -1, -1):
            T[i] = cost[i] + min(T[i+1], T[i+2])
            
        return min(T[0], T[1])