class Solution:
    def climbStairs(self, n: int) -> int:


        cache = {}

        def recurse(current):

            if current == n:
                return 1
            
            if current > n:
                return 0
            
            if current in cache:
                return cache[current]
            
            cache[current] = recurse(current + 1) + recurse(current + 2)
            return cache[current]
        
        return recurse(0)
        
