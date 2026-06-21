class Solution:
    def grayCode(self, n: int) -> List[int]:
        



        def recurse(n):
        
            if n == 1:
                return ["0", "1"]

            nMinusOne = recurse(n - 1)
            masterList = ["0" + code for code in nMinusOne] + ["1" + code for code in nMinusOne][::-1]
            return masterList
        

        return [int(x, 2) for x in recurse(n)]






