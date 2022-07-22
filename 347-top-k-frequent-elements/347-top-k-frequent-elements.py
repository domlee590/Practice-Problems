class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)
        minheap = []

        for num, freq in freqMap.items():
            heappush(minheap, (freq, num))
            if len(minheap) > k:
                heappop(minheap)

        topK = []
        for _ in range(k):
            topK.append(heappop(minheap)[1])

        return topK