import time
from algorithms.algorithm import Algorithm

class QuickSort(Algorithm):
    def __init__(self, size=100):
        super().__init__(size)

    def sort(self, drawData, timeTick):
        self._sort(0, len(self.data)-1, drawData, timeTick)

    def _sort(self, start, end, drawData, timeTick):
        if start < end:
            mid = (start + end) // 2
            pivot = self.data[mid]
            l,r = start, end
            while l<=r:
                while l<=r and self.data[l]<pivot:
                    l+=1
                while l<=r and self.data[r]>pivot:
                    r-=1
                if l<=r:
                    self.data[l],self.data[r] = self.data[r],self.data[l]
                    l+=1; r-=1
            
            self._sort(start, r, drawData, timeTick)
            self._sort(l, end, drawData, timeTick)
        
            drawData(self.data, [self.color.PURPLE if x >= start and x < mid else self.color.YELLOW if x == mid 
                            else self.color.DARK_BLUE if x > mid and x <=end else self.color.BLUE for x in range(len(self.data))])
            time.sleep(timeTick)

        drawData(self.data, [self.color.BLUE for x in range(len(self.data))])
