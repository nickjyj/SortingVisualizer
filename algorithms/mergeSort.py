import time
from colors import *

def merge(data, start, end, mid):
    tmp = []
    i,j = start,mid+1
    while i<=mid or j<=end:
        v1 = data[i] if i<=mid else float('inf')
        v2 = data[j] if j<=end else float('inf')
        if v1<v2:
            tmp.append(v1)
            i+=1
        else:
            tmp.append(v2)
            j+=1
    for i in range(start,end+1):
        data[i] = tmp[i-start]


def merge_sort(data, start, end, drawData, timeTick):
    if start < end:
        mid = (start + end) // 2
        merge_sort(data, start, mid, drawData, timeTick)
        merge_sort(data, mid+1, end, drawData, timeTick)
        
        merge(data, start, end, mid)
    
        drawData(data, [PURPLE if x >= start and x < mid else YELLOW if x == mid 
                        else DARK_BLUE if x > mid and x <=end else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])
