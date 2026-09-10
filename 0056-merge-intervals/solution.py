class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []

        i = 0

        while i < len(intervals):

            if not result:
                result.append(intervals[0])
                i += 1
                continue
            
            current_interval = intervals[i]
            if current_interval[0] <= result[-1][1]:
                result[-1] = [min(current_interval[0], result[-1][0]), max(current_interval[1], result[-1][1])]
                i += 1
            else:
                result.append(intervals[i])
        
        return result
        
