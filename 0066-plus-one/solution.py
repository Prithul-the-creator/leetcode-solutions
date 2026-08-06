class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digit = len(digits) - 1
        i = 0

        while digit - i >= 0 and digits[digit - i] == 9:
            digits[digit - i] = 0
            if not digit - i - 1 >= 0:
                digits.insert(0, 1)
                return digits
            i += 1
        
    
        digits[digit - i] += 1
        
    
        return digits


        
