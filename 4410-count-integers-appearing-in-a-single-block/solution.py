class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:

        seen = {}
        not_special = set()
        result = len(set(nums))

        for i in range(len(nums)):

            if nums[i] not in seen:
                seen[nums[i]] = i
            else:
                if i != seen[nums[i]] + 1 and nums[i] not in not_special:
                    result -= 1
                    not_special.add(nums[i])

                seen[nums[i]] = i

        return result
