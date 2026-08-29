class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result = []

        def recurse(i, path):

            if i >= len(s):
                result.append(path[:])
                return
            for j in range(i, len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    path.append(s[i:j + 1])
                    recurse(j + 1, path)
                    path.pop()

        recurse(0, [])
        return result
                
            
            
                      



        
