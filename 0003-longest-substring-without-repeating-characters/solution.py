class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)

        
        
        result = 1
        letters = {s[0]}

        i, j = 0, 1

        while j < len(s):
            
            if s[j] in letters:
                while s[i] != s[j]:
                    letters.remove(s[i])
                    i += 1
                i += 1
                j += 1
            
            else:
                result = max(result, j - i + 1)
                letters.add(s[j])
                j += 1
        
        return result



            








        
