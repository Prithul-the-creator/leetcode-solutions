class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)

        visited = set()
        added = set()
        result = []
        def dfs(course):

            if course in visited:
                return False
            if course not in adj:
                return True

            visited.add(course)
            
            for i in range(len(adj[course])):
                if not dfs(adj[course][i]):
                    return False
            
            if course not in added:
                result.append(course)
            added.add(course)
            visited.remove(course)
            
            adj[course] = []
            
            return True
        
        for course in adj:
            if not dfs(course): return []
        return result
            








        
