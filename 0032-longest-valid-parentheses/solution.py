class Solution:
    def longestValidParentheses(self, string: str) -> int:

        l, r = 0, 0
        result1 = 0
        current = 0

        for char in string:

            if char == "(":
                l += 1
                current += 1
            else:
                r += 1
                current += 1
            
            if l == r:
                result1 = max(result1, current)
            elif r > l:
                l, r = 0, 0
                current = 0
        print(result1)
        
        l, r = 0, 0
        result2 = 0
        current = 0

        for char in string[::-1]:

            if char == "(":
                l += 1
                current += 1
            else:
                r += 1
                current += 1
            
            if l == r:
                result2 = max(result2, current)
            elif r < l:
                l, r = 0, 0
                current = 0
        print(result2)
        
        
        return max(result1, result2)
            

        
