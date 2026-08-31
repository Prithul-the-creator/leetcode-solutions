class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums) == 2:
            return nums.index(max(nums))
        l, r = 0, len(nums) - 1

        while r >= l:

            mid = l + (r - l) // 2
            if mid == 0 or mid == len(nums) - 1 or nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        


        
        
