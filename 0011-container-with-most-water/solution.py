class Solution:
    def maxArea(self, height: List[int]) -> int:



        l, r = 0, len(height) - 1
        result = 0



        while r > l:
            result = max(result, abs(min(height[l], height[r]) * (r - l)))

            if height[r] >= height[l]:
                l += 1
            else:
                r -= 1

        return result



            

        
