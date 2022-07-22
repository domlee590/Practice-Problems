class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap, result = [], []

        for point in points:
            distance = (point[0]) ** 2 + (point[1]) ** 2
            heap.append((distance, point))

        heapify(heap)
        for _ in range(k):
            result.append(heappop(heap)[1])

        return result