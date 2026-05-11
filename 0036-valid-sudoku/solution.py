class Solution:
    def isValidSudoku(self, grid: List[List[str]]) -> bool:

        def square(i, j):
            visited = set()
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    print(r, c)
                    if grid[r][c] == ".":
                        continue
                    if grid[r][c] not in visited:
                        visited.add(grid[r][c])
                    else:
                        return 1
            return 0


        def row(i, j):

            visited = set()
            for j in range(9):

                if grid[i][j] == ".":
                    continue
                if grid[i][j] not in visited:
                    visited.add(grid[i][j])
                else:
                    return 1
            return 0


        def column(i, j):

            visited = set()
            for i in range(9):

                if grid[i][j] == ".":
                    continue
                if grid[i][j] not in visited:
                    visited.add(grid[i][j])
                else:
                    return 1
            return 0


        result = 0
        for i in range(9):
            result += row(i, 0)
        
        for j in range(9):
            result += column(0, j)
        
        row = 0
        col = 0
        for z in range(9):
            if z%3 == 0 and z != 0:
                row += 1
                col = 0
            result += square(3 * row, col)
            col += 3
        
        if result:
            return False
        return True




        

        


        
