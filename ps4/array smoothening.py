from heapq import heappop,heappush, heapify
from collections import Counter, OrderedDict
n, m = map(int, input().split())
arr = sorted([int(i) for i in input().split()])
freq = dict(Counter(arr))



#max value:
#less than n-m

pq = sorted((-v,k) for k,v in freq.items())[:m+1]
heapify(pq)
tmp = 0
while m > 0:
    tmp = heappop(pq)
    if tmp == 0:
        break
    value = tmp[0] + 1
    if value < 0:
        heappush(pq,(value, tmp[1]))
    m -= 1
if m == n:
    print(0)
elif tmp == 0:
    print(1)
else:
    print(-heappop(pq)[0])












