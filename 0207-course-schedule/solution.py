class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        adj_list = {pre: [] for pre in range(numCourses)}
        for course, pre in prerequisites:
            adj_list[pre].append(course)
        
        visited = set()
        temp = set()


        def dfs(node):
            if node in temp:
                return False
            if node in visited:
                return True
            visited.add(node)
            temp.add(node)

            for edge in adj_list[node]:
                if not dfs(edge):
                    return False

            temp.remove(node)
            return True
        
        for i in range(len(adj_list)):
            if i in visited:
                continue
            if not dfs(i):
                return False
        return True
