class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        i, j = 0, len(numbers) - 1

        currentSum = numbers[i] + numbers[j]

        while j > i:

            if currentSum < target:
                i += 1
                currentSum = numbers[i] + numbers[j]
            elif currentSum > target:
                j -= 1
                currentSum = numbers[i] + numbers[j]
            else:
                break
            
        
        return [i + 1, j + 1]





        
