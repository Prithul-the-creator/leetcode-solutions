class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        
        while True:
            result = 1
            current = [int(char) for char in str(n)]
            for number in current:
                result *= number
            
            if result % t == 0:
                return n
            
            n += 1

