class Solution:
    def rob(self, nums: List[int]) -> int:
        # Keep track of the maximum profit robbing up to previous 2 houses
        # rob1 is 2 houses ago, rob2 is one house ago
        rob1, rob2 = 0, 0
        
        # Compute max profit robbing up to n
        for n in nums:
            # Rob current and add those before, skip current and maintain last house
            curProfit = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = curProfit
        
        return rob2