import heapq
from heapq import heapify, heappush, heappop
from math import sqrt

#kClosest - done by me
def kClosest(points, k):
    res = []
    final =[]
    heapify(res)
    for item in points:
        dist = sqrt((item[0] **2 + item[1] **2))
        heappush(res,(dist,item))
    for _ in range(k):
        final.append(heappop(res)[1])
    return final
print(kClosest([[1,3],[-2,2]],1))
print(kClosest([[3,3],[5,-1],[-2,4]],2))

from heapq import heapify, heappush, heappop
from collections import Counter
def leastInterval(task,n):
    if n == 0:
        return len(task)
    occur = Counter(task).values()
    heap = []
    for count in occur:
        heapq.heappush(heap,-count)
    time, tmp = 0, []
    while heap:
        for _ in range(n+1):
            if heap or tmp:
                time += 1
            if heap:
                count = heapq.heappop(heap)