class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj_list[course].append(pre)

        visited = set()
        temp = set()
        result = []
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
            result.append(node)
            return True

        for i in range(numCourses):
            if i in visited:
                continue
            if not dfs(i):
                return []
        return result
            
            

            


            








        
