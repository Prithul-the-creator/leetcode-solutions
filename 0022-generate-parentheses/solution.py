class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []


        def dfs(string, nopen, nclosed):

            if nopen == n and nclosed == n:
                result.append(string)
                return
            
            if nclosed > nopen or nopen > n or nclosed > n:
                return
            
            dfs(string + "(", nopen + 1, nclosed)
            dfs(string + ")", nopen, nclosed + 1)



        dfs("", 0, 0)
        return result


            


        
