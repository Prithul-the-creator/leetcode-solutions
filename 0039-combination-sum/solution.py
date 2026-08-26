class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = set()

        def dfs(current, remaining):
            
            if remaining < 0:
                return
            if remaining == 0:
                result.add(tuple(sorted(current)))
            
            for i in range(len(candidates)):
                current.append(candidates[i])
                dfs(current, remaining - candidates[i])
                current.pop()

        dfs([], target)
        return list(result)
        
