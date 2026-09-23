class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        heap = []
        for x, y in points:
            heapq.heappush(heap, (math.sqrt(x**2 + y**2), x, y))
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1:])
        return result
