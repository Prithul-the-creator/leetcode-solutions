class Solution:
    def minimumPushes(self, word: str) -> int:
        


        return sum([number // 8 + 1 for number in range(len(word))])




        
