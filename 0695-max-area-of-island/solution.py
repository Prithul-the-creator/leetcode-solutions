class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        result = 0 
        
        

        def bfs(i, j):
            count = 0
            q = deque()
            q.append((i, j))
            visited.add((i, j))

            while q:
                
                i, j = q.popleft()
                count += 1
                neighbors = [[0, 1], [0, -1], [-1, 0], [1, 0]]
                for dr,dc in neighbors:
                    if i + dr < 0 or i + dr >= len(grid) or j + dc < 0 or j + dc >= len(grid[0]) or grid[i + dr][j + dc] == 0 or (i + dr, j + dc) in visited:
                        continue
                    q.append((i  + dr, j + dc))
                    visited.add((i  + dr, j + dc))
                

            return count
            
        
        visited = set()
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    result = max(result, bfs(i, j))

        return result
