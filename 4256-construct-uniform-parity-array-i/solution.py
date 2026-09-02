class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        return True

        result1 = []
        result2 = []

        for i in range(len(nums)):

            if nums[i] % 2 == 1:
                result1.append(True)
                for j in range(len(nums)):
                    if i != j:
                        if abs(nums[i] - nums[j]) % 2 == 1:
                            result2.append(True)
            else:
                for j in range(len(nums)):
                    if i != j:
                        if abs(nums[i] - nums[j]) % 2 == 1:
                            result1.append(True)
                result2.append(True)
        
        return len(result1) == len(nums) or len(result2) == len(nums)
            

        
