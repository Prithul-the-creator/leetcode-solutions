class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        candidates.sort()

        def dfs(index, current, remaining):
            print(index, current, remaining)
            if remaining == 0:
                result.append(current[:])
                return
            
            if remaining < 0 or index >= len(candidates):
                return
            
            current.append(candidates[index])
            dfs(index + 1, current, remaining - candidates[index])
            current.pop()
            while index < len(candidates) - 1 and candidates[index + 1] == candidates[index]:
                index += 1
            dfs(index + 1, current, remaining)
        
        dfs(0, [], target)
        return result
            

        
