class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == "0":
            return 0
        cache  = {}
        def recurse(i):

            if i >= len(s):
                return 1
            if int(s[i]) == 0:
                return 0
            if i in cache:
                return cache[i]

            a = recurse(i + 1)
            b = 0
            if i + 1 < len(s) and 1 <= int(s[i:i + 2]) <= 26:
                b = recurse(i + 2)
            cache[i] = a + b
            return cache[i]
        recurse(0)
        return cache[0]
                 
        




        
