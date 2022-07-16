class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maxProf = 0
        
        for price in prices[1:]:
            if price < lowest:
                lowest = price
            elif price - lowest > maxProf:
                maxProf = price - lowest
            
        return maxProf