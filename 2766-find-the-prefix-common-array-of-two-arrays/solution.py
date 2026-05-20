class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:


        result = []
        visited = set()
        current = 0

        for i, j in zip(A, B):
            
            if i in visited or i == j:
                current += 1
            if j in visited:
                current += 1
            
            visited.add(i)
            visited.add(j)
            result.append(current)
        
        return result
                


        


