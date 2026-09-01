class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counter = dict(Counter(tasks))
        heap = [[-b, a] for a, b in counter.items()]
        heapq.heapify(heap)

        count = 0
        in_process = {}
        
        while heap:
            removed = []
            while heap:
                current = heapq.heappop(heap)
                removed.append(current)
                if current[1] not in in_process:
                    current[0] += 1
                    if current[0] == 0:
                        removed.pop()
                    if current[0] != 0:
                        in_process[current[1]] = n + 1
                    break
            count += 1
            for remove in removed:
                heapq.heappush(heap, remove)
                    
            for process in list(in_process):
                in_process[process] -= 1
                if in_process[process] == 0:
                    del in_process[process]
            
        return count
                

