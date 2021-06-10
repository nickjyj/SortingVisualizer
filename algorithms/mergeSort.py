import time
from algorithms.algorithm import Algorithm

class MergeSort(Algorithm):
    def __init__(self, size=100):
        super().__init__(size)

    def merge(self, start, end, mid):
        tmp = []
        i,j = start,mid+1
        while i<=mid or j<=end:
            v1 = self.data[i] if i<=mid else float('inf')
            v2 = self.data[j] if j<=end else float('inf')
            if v1<v2:
                tmp.append(v1)
                i+=1
            else:
                tmp.append(v2)
                j+=1
        for i in range(start,end+1):
            self.data[i] = tmp[i-start]

    def sort(self, drawData, timeTick):
        self._sort(0, len(self.data)-1, drawData, timeTick)

    def _sort(self, start, end, drawData, timeTick):
        if start < end:
            mid = (start + end) // 2
            self._sort(start, mid, drawData, timeTick)
            self._sort(mid+1, end, drawData, timeTick)
            
            self.merge(start, end, mid)
        
            drawData(self.data, [self.color.PURPLE if x >= start and x < mid else self.color.YELLOW if x == mid 
                            else self.color.DARK_BLUE if x > mid and x <=end else self.color.BLUE for x in range(len(self.data))])
            time.sleep(timeTick)

        drawData(self.data, [self.color.BLUE for x in range(len(self.data))])
