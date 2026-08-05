class MedianFinder:

    def __init__(self):
        self.bottom = []
        self.top = []
        
        

    def addNum(self, num: int) -> None:
        if not self.bottom:
            heapq.heappush(self.bottom, -num)
            return
    
        if num > -self.bottom[0]:
            heapq.heappush(self.top, num)
            if len(self.top) - len(self.bottom) == 2:
                item = heapq.heappop(self.top)
                heapq.heappush(self.bottom, -item)
        else:
            heapq.heappush(self.bottom, -num)
            if len(self.bottom) - len(self.top) == 2:
                item = -heapq.heappop(self.bottom)
                heapq.heappush(self.top, item)
           

        

    def findMedian(self) -> float:


        if len(self.bottom) > len(self.top):
            return -self.bottom[0]
        elif len(self.bottom) < len(self.top):
            return self.top[0]
        else:
            return (-self.bottom[0] + self.top[0])/2



        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
