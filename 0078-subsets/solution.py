class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        def dfs(current, remaining):
            nonlocal result
            if not remaining:
                result.append(current[:])
                return
            
            current.append(remaining[0])
            dfs(current, remaining[1:])
            current.pop()
            dfs(current, remaining[1:])
            
        
        dfs([], nums)
        
        return result
        
