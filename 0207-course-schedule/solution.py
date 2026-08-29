class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[course].append(pre)
        
        visited = set()
        result = True
        def dfs(course, path):
            nonlocal result
            if course in path:
                result = False
                return
            if course not in adj or course in visited:
                return

            path.add(course)
            for i in range(len(adj[course])):
                dfs(adj[course][i], path)
            path.remove(course)
            visited.add(course)
        
        for course in adj:
            dfs(course, set())
        
        return result
            








        
