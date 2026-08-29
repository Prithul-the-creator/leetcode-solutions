class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        table = {1:"", 2: "abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7: "pqrs", 8:"tuv", 9:"wxyz"}
        result = []
        def dfs(index, path):

            if index >= len(digits):
                result.append("".join(path))
                return

            current = table[int(digits[index])]
            for i in range(len(current)):
                dfs(index + 1, path + [current[i]])
                
        dfs(0, [])
        return result





        
