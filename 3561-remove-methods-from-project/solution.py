class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:


        adjacency_list = defaultdict(set)


        for a, b in invocations:
            adjacency_list[a].add(b)


        visited = set()
        def dfs(key):
            nonlocal visited
            if key in visited:
                return
            
            visited.add(key)

            for k in adjacency_list[key]:
                dfs(k)

        dfs(k)
        
        for key in adjacency_list:

            if key in visited:
                continue
            
            for k in adjacency_list[key]:
                if k in visited:
                    return list(range(n))
        

        result = set(list(range(n)))
        for key in visited:
            result.remove(key)
        
        return list(result)




        
