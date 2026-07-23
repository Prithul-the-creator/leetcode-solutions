class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        result = []
        intervals.sort(key = lambda x: x[0])

        start, end = intervals[0]

        for current_start, current_end in intervals[1:]:

            if current_start <= end:
                end = max(end, current_end)
            else:
                result.append([start, end])
                start, end = current_start, current_end
        
        result.append([start, end])
        print(result)

        return result






        
