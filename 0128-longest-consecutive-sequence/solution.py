class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        nums = set(nums)
        visited = set()

        
        longeststreak = 1
        for number in nums:
            if number in visited:
                continue
            currentstreak = 1
            i = 1
            while True:
                if number + i in nums:
                    visited.add(number + i)
                    currentstreak += 1
                    i += 1
                else:
                    break
            
            longeststreak = max(longeststreak, currentstreak)
        
        return longeststreak




        
