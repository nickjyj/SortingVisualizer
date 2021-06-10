import time
from colors import *

def quick_sort(data, start, end, drawData, timeTick):
    if start < end:
        mid = (start + end) // 2
        pivot = data[mid]
        l,r = start, end
        while l<=r:
            while l<=r and data[l]<pivot:
                l+=1
            while l<=r and data[r]>pivot:
                r-=1
            if l<=r:
                data[l],data[r] = data[r],data[l]
                l+=1; r-=1
        
        quick_sort(data, start, r, drawData, timeTick)
        quick_sort(data, l, end, drawData, timeTick)
    
        drawData(data, [PURPLE if x >= start and x < mid else YELLOW if x == mid 
                        else DARK_BLUE if x > mid and x <=end else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])
