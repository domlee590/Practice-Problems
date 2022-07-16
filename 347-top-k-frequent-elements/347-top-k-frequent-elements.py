class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [[] for _ in range(len(nums) + 1)]
        freq = dict()
        
        for char in nums:
            freq[char] = 1 + freq.get(char, 0)
        for char, times in freq.items():
            res[times].append(char)
        
        topK = []
        for i in range(len(res)-1, 0, -1):
            for num in res[i]:
                topK.append(num)
            if len(topK) == k:
                return topK