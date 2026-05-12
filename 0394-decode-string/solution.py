class Solution:
    
    
    def decodeString(self, s: str) -> str:
        
        def recurse(string, result):

            if "[" not in string:
                return string

            start = -1
            ending = -1
            currentweight = -1
            i = 0
            while i < len(string):

                if (
                    i + 1 < len(string)
                    and string[i].isdigit()
                    and string[i + 1] == "["
                ):
                    j = i
                    while j > 0 and string[j - 1].isdigit():
                        j -= 1
                    currentweight = int(string[j:i + 1])

                elif string[i] == "[":
                    start = i

                    balance = 1
                    j = i + 1

                    while j < len(string):
                        if string[j] == "[":
                            balance += 1
                        elif string[j] == "]":
                            balance -= 1

                        if balance == 0:
                            ending = j
                            break

                        j += 1

                    result += currentweight * recurse(string[start + 1: ending], "")
                    i = ending
                    start = -1
                    ending = -1
                    currentweight = -1
                    
                elif start == -1 and string[i].isalpha():
                    result += string[i]

                
                i += 1

            return result

        return recurse(s, "")

        
    
    
