class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:


        dp = [1] * (len(nums) + 1)
        result = 1
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
            result = max(result, dp[i])
        
        return result

        
