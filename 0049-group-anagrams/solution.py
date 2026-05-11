class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        
        counterdict = {}
        


        for word in strs:

            sortedword = "".join(sorted(word))

            if sortedword in counterdict:
                counterdict[sortedword].append(word)
            else:
                counterdict[sortedword] = [word]
            

        return list(counterdict.values())




        
