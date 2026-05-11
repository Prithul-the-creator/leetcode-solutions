class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counters = dict(Counter(s))
        countert = dict(Counter(t))

        for key in counters:
            if key not in countert:
                return False
            elif counters[key] != countert[key]:
                return False
        
        return True



        






        
