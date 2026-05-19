class Solution:
    def reverse(self, x: int) -> int:

        
        if x < 0:
            string = ""
            curr = -1 * x
            while curr > 0:
                string += str(curr % 10)
                curr //= 10

            if not (-1 * 2 ** 31 < -1 * int(string) < 2 ** 31 - 1):
                return 0

            return -1 * int(string)

        string = "0"

        while x > 0:
            string += str(x % 10)
            x //= 10
        
        if not (-1 * 2 ** 31 < int(string) < 2 ** 31 - 1):
            return 0
        return int(string)
        
