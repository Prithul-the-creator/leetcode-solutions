class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        time = 0
        q = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    visited.add((i, j))
        
        while q:

            r, c, current_time = q.popleft()
            time = max(current_time, time)

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                if r + dr < 0 or c + dc < 0 or r + dr >= len(grid) or c + dc >= len(grid[0]) or (r + dr, c + dc) in visited or grid[r + dr][c + dc] == 0:
                    continue
                q.append((r + dr, c + dc, current_time + 1))
                visited.add((r + dr, c + dc))
                

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] >= 1 and (i, j) not in visited:
                    return -1
        
        return time
        
        




        



        
        
