class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[course].append(pre)
        
        visited = set()

        def dfs(course):

            if course in visited:
                return False
            if course not in adj:
                return True

            visited.add(course)
            for i in range(len(adj[course])):
                if not dfs(adj[course][i]):
                    return False
            visited.remove(course)
            adj[course] = []
            return True
        
        for course in adj:
            if not dfs(course): return False
        
        return True
            








        
