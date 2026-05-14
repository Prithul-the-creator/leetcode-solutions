class Solution:
    def isPalindrome(self, s: str) -> bool:


        newstring = ""

        for char in s:
            if char.isalnum():
                newstring += char.lower()
        

        return newstring == newstring[::-1]
        
