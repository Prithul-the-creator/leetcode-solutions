class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

            current = 0
            result = 0
            for j in range(len(nums)):

                if nums[j] == 1:
                    current += 1
                    result = max(result, current)
                
                else:
                    current = 0
            
            return result


