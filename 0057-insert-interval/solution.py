class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]
        result = []

        found = False
        for start, end in intervals:

            if newInterval[0] <= end and start <= newInterval[1] and not found:
                result.append([min(start, newInterval[0]), max(end, newInterval[1])])
                found = True
            else:
                if not result:
                    result.append([start, end])
                else:
                    if start > result[-1][1]:
                        result.append([start, end])
                    else:
                        result[-1] = [min(start, result[-1][0]), max(end, result[-1][1])]
        if not found:
            result.append(newInterval)
            result.sort(key = lambda x: x[0])
            
        return result


