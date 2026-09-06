class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [tasks[i] + [i] for i in range(len(tasks))]
        tasks.sort()
        time, index = 1, 0
        heap, result = [], []

        while heap or index < len(tasks):

            if not heap and time < tasks[index][0]:
                time = tasks[index][0]

            while index < len(tasks) and tasks[index][0] <= time:
                heapq.heappush(heap, (tasks[index][1], tasks[index][2], tasks[index][0]))
                index += 1
            if heap:
                processing_time, cindex, enque_time = heapq.heappop(heap)
                result.append(cindex)
                time += processing_time
            
            
        
        return result
