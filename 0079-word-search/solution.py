class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        result = False
        visited = set()

        def dfs(i, j, index):
            nonlocal result
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or (i, j) in visited or board[i][j] != word[index]:
                return
            
            if index == len(word) - 1:
                result = True
                return
            visited.add((i, j))
            dfs(i + 1, j, index + 1) or dfs(i - 1, j, index + 1) or dfs(i, j + 1, index + 1) or dfs(i, j - 1, index + 1)
            visited.remove((i, j))

        

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    dfs(i, j, 0)
        
        return result
        
