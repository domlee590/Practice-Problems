class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # Create tabulation array (LIS starting at index)
        # Base case is last index, which must be length 1
        T = [1 for _ in range(len(nums))]
        
        # Start iterating from second to last starting index
        for i in range(len(nums) - 1, -1, -1):
            # Check if we can combine the subsequences (latter starts larger)
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    T[i] = max(T[i], 1 + T[j])
        
        # Get the largest subsequence starting at some index
        return max(T)