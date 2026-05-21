class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        hashset = set()

        for number in arr2:

            string = str(number)

            for i in range(1, len(string) + 1):
                hashset.add(int(string[0:i]))
        
        result = 0
        for n in arr1:
            while n and n not in hashset:
                n = n // 10
            
            if n:
                result = max(result, len(str(n)))


        return result
