class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        hashset = set()

        for num in range(len(boxes)):
            if boxes[num] == "1":
                hashset.add(num)

        result = []
        for i in range(len(boxes)):
            current = 0
            for num in hashset:
                if num != i:
                    current += abs(i - num)
            
            result.append(current)
        
        return result

        
