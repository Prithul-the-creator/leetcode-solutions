class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        

        def gcd(a, b):
            return math.gcd(a, b)
    
        if len(nums) < 2:
            return 0

        gcdArray = [nums[0]]
        current_largest = nums[0]

        for i in range(1, len(nums)):

            if nums[i] > current_largest:
                current_largest = nums[i]

            gcdArray.append(gcd(nums[i], current_largest))
        
        result = 0
        gcdArray.sort()

        for i in range(len(gcdArray)//2):
            result += gcd(gcdArray[i], gcdArray[-i - 1])

        return result


