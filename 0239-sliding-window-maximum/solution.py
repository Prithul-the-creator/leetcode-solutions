class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        max_heap = [-x for x in nums[:k]]
        heapq.heapify(max_heap)
        elements = dict(Counter(nums[:k]))
        results = [-max_heap[0]]
        

        for i in range(1, len(nums) - k + 1):
            elements[nums[i - 1]] -= 1
            if nums[i + k - 1] not in elements:
                elements[nums[i + k - 1]] = 0
            elements[nums[i + k - 1]] += 1
            heapq.heappush(max_heap, -nums[i + k - 1])
        

            while max_heap:
                current = -heapq.heappop(max_heap)
                if elements[current] > 0:
                    heapq.heappush(max_heap, -current)
                    results.append(current)
                    break

        
        return results




            


        
