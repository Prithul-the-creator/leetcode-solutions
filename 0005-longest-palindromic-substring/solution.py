class Solution:
    def longestPalindrome(self, s: str) -> str:


        result = s[0]
        largest = 1

        for i in range(len(s)):

            a,b = i, i

            while a > -1 and b < len(s) and s[a] == s[b]:
                if b - a + 1 > largest:
                    largest = b - a + 1
                    result = s[a:b + 1]
                a -= 1
                b += 1
            
            a, b = i, i + 1
            while a > -1 and b < len(s) and s[a] == s[b]:
                if b - a + 1 > largest:
                    largest = b - a + 1
                    result = s[a:b + 1]
                a -= 1
                b += 1
            
        return result
        
