class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:


        distances = {vertex: float("inf") for vertex in range(1, n + 1)}
        distances[k] = 0
        heap = [(0, k)]

        adj_list = {i:[] for i in range(1, n + 1)}
        for prev, to, weight in times:
            adj_list[prev].append((to, weight))

        while heap:
            distance, u = heapq.heappop(heap)
            if distance > distances[u]:
                continue
            edges = adj_list[u]

            for v, edge_weight in edges:

                if distances[v] > distances[u] + edge_weight:
                    distances[v] = distances[u] + edge_weight
                    heapq.heappush(heap, (distances[v], v))
        result = 0
        for distance in distances.values():
            if distance == float("inf"):
                return -1
            result = max(result, distance)
        return result
        








            



        
