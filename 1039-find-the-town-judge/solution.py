class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        
        if len(trust) < n - 1:
            return -1

        if not trust or n == 1:
            return 1

        visited = set()

        adjacencyList = {}
        endpoints = []
        
        for a, b in trust:
            visited.add(a)
            visited.add(b)
            endpoints.append(b)
            
            if a not in adjacencyList:
                adjacencyList[a] = [b]
            else:
                adjacencyList[a].append(b)
        

        counter = dict(Counter(endpoints))
        for count in counter:
            if counter[count] == n - 1 and count not in adjacencyList:
                return count
        
        return -1

        
