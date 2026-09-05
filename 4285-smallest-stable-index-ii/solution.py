class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        smallest, largest = [nums[-1]], [nums[0]]
        for i in range(1, len(nums)):
            largest.append(max(nums[i], largest[-1]))
            smallest.append(min(nums[len(nums) - 1 - i], smallest[-1]))
        smallest = smallest[::-1]
        
        for i in range(len(nums)):
            if largest[i] - smallest[i] <= k:
                return i
        return -1
