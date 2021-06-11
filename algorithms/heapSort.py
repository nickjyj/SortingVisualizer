import time
from algorithms.algorithm import Algorithm

class HeapSort(Algorithm):
    def __init__(self, size=100):
        super().__init__(size)

    def sort(self, drawData, timeTick):
        self._sort(len(self.data), drawData, timeTick)

    def _sort(self, n, drawData, timeTick):
        def heapify(n, i):
            largest = i
            l,r = 2*i+1, 2*i+2
            if l < n and self.data[largest] < self.data[l]:
                largest = l
            if r < n and self.data[largest] < self.data[r]:
                largest = r
            if largest != i:
                self.data[i],self.data[largest] = self.data[largest],self.data[i]
                drawData(self.data, [self.color.YELLOW if x == i or x == 0 else self.color.BLUE for x in range(len(self.data))] )
                time.sleep(timeTick)
                heapify(n, largest)
        
        # build max heap
        for i in range(n//2,-1,-1):
            heapify(n, i)
        
        # sorting
        for i in range(n-1,0,-1):
            self.data[0],self.data[i] = self.data[i],self.data[0]
            drawData(self.data, [self.color.YELLOW if x == i or x == 0 else self.color.BLUE for x in range(len(self.data))] )
            time.sleep(timeTick)
            heapify(i,0)
        