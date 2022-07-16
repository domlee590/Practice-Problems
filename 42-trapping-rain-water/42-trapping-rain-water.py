class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        total = 0
        lMax = 0
        rMax = 0
        
        while(left < right):
            #water is dependent on shortest bar on a side
            
            #if left side shorter, depend on left
            if height[left] < height[right]:
                if height[left] > lMax:
                    lMax = height[left] 
                else:
                    total += lMax - height[left]
                left += 1
            
            #if right side shorter, depend on right
            else:
                if height[right] > rMax:
                    rMax = height[right]
                else:
                    total += rMax - height[right]
                right -= 1
        
        return total