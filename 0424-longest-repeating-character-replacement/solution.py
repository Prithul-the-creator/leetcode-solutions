class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        result = 1
        l, r = 0, 1
        counter = defaultdict(int)
        counter[s[l]] = 1

        while r < len(s):

            counter[s[r]] += 1

            current_max = 1
            for count in counter:
                current_max = max(current_max, counter[count])
            
            if current_max + k < r - l + 1:
                while current_max + k < r - l + 1:
                    counter[s[l]] -= 1
                    l += 1
            
            else:
                result = max(result, min(current_max + k, len(s)))
            r += 1
        
        return result








        
