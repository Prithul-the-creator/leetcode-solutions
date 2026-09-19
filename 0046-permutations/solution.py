class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:



        result = []

        def swap(i):
            
            if i == len(nums) - 1:
                result.append(nums[:])
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                swap(i + 1)
                nums[i], nums[j] = nums[j], nums[i]
            

        swap(0)
        return result


        
