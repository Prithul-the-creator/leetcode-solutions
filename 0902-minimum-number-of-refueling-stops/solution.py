import heapq
class Solution:

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:


        refuels = -1
        curr_distance = 0
        heap = []
        heapq.heappush(heap, -1*startFuel)

        while curr_distance < target:

            if not heap:
                return -1

            add_miles = -1 * heapq.heappop(heap)
            print(add_miles)
            refuels += 1

            curr_distance += add_miles

            while stations:
                if stations[0][0] <= curr_distance:
                    heapq.heappush(heap, -1 * stations[0][1])
                    del stations[0]
                    
                else:
                    break
            
            
        
        return refuels
        
        
