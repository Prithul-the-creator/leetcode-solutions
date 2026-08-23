class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:\

        visited = set()
        result = 0
        
        def dfs(i, j):
            nonlocal visited
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i, j) in visited or grid[i][j] == "0":
                return

            visited.add((i, j))
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    result += 1
                    dfs(i, j)

        return result
