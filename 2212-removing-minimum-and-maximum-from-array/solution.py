class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1
        result = 0
        smallest = nums.index(min(nums))
        largest = nums.index(max(nums))
        #print(smallest, largest)
        smallest_index = min(smallest, largest) + 1
        largest_index = len(nums) - max(smallest, largest)
        #print(smallest_index, largest_index)

        print(min(smallest_index, largest_index), min(max(smallest, largest) - min(smallest, largest) + 1, max(smallest_index, largest_index)))
        result += min(smallest_index, largest_index)
        result += min(max(smallest, largest) - min(smallest, largest), max(smallest_index, largest_index))

        return result




        


