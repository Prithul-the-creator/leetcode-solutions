class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        def dfs(current, remaining):
            nonlocal result
            if not remaining:
                result.add(tuple(current[:]))
                return
            
            current.append(remaining[0])
            dfs(current, remaining[1:])
            
            current.pop()
            dfs(current, remaining[1:])
            
        
        dfs([], nums)
        
        return list(result)
