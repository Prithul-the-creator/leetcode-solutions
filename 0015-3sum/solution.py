class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        result = set()
        visited = set()

        for k in range(len(nums) - 2):

            if nums[k] in visited:
                continue
            visited.add(nums[k])
            target = 0 - nums[k]
            
            i, j = k + 1, len(nums) - 1
            currentSum = nums[i] + nums[j]

            while j > i:
                
                if currentSum < target:
                    i += 1
                    currentSum = nums[i] + nums[j]
                elif currentSum > target:
                    j -= 1
                    currentSum = nums[i] + nums[j]
                else:
                    result.add((nums[k], nums[i], nums[j]))
                    j -= 1
                    currentSum = nums[i] + nums[j]
        
        return [list(thing) for thing in result]
                    
