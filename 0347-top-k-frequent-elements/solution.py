class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        counter = dict(Counter(nums))

        result = []
        values = list(counter.items())
        values.sort(key = lambda x: x[1], reverse = True)
        return [x[0] for x in values[:k]]
        

        
