class Solution:
    def countAndSay(self, n: int) -> str:
        def RLE(string):
            if string == "1":
                return "11"

            result = ""
            count = 1
            for i in range(len(string) - 1):

                if string[i] == string[i + 1]:
                    count += 1
                else:
                    result += (str(count) + string[i])
                    count = 1

            if count == 1:
                result += (str(count) + string[-1])
            else:
                #count += 1
                result += (str(count) + string[i])
            print(result)
            return result

        def count(n):
            if n == 1:
                return "1"
            
            return RLE(count(n - 1))
        
        return count(n)
        
    
        
