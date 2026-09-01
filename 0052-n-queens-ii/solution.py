class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:

        result = 0
        board = [["."]*n for i in range(n)]
        rows, cols, posdiag, negdiag = set(), set(), set(), set()
        def dfs(i, j, queens):
            nonlocal result
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or i in rows or j in cols or i-j in posdiag or i + j in negdiag:
                return
            

            board[i][j] = "Q"
            if queens == n:
                result += 1
                board[i][j] = "."
                return
            rows.add(i)
            cols.add(j)
            posdiag.add(i - j)
            negdiag.add(i + j)

            for down in range(n):
                dfs(down, j + 1, queens + 1)

            board[i][j] = "."
            rows.remove(i)
            cols.remove(j)
            posdiag.remove(i - j)
            negdiag.remove(i + j)
        
        for row in range(n):
            dfs(row, 0, 1)
        return result
        
