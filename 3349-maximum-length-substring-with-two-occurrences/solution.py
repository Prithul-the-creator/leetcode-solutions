class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        def maxSubarrayLength(nums, k):
            nums = list(nums)
            if len(nums) <= 1:
                return 1
            
            counter = defaultdict(int)
            counter[nums[0]] = 1
            result = 1
            l, r = 0, 1

            while r < len(nums):
                if counter[nums[r]] >= k:
                    while nums[l] != nums[r]:
                        counter[nums[l]] -= 1
                        l += 1
                    counter[nums[l]] -= 1
                    l += 1
                else:
                    result = max(result, r - l + 1)
                    counter[nums[r]] += 1
                    r += 1
            
            return result
        

        return maxSubarrayLength(s, 2)



        
