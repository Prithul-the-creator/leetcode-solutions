class Solution:
    def reverseWords(self, s: str) -> str:


        s = s.strip()

        i, j = 0, 0
        currentword = ""
        wordlist = []

        while j < len(s):

            if s[j].isalnum():
                currentword = s[i : j + 1]
                j += 1
            
            else:
                if currentword:
                    wordlist.append(currentword.strip())
                i = j
                j += 1
                currentword = ""
        
        if currentword:
            wordlist.append(currentword.strip())


        return " ".join(wordlist[::-1])


            






        
