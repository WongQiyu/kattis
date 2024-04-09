from math import inf
from heapq import heappush,heappop

A, H = map(int, input().split())
n,m = map(int, input().split())

AL = [[] for _ in range(n)]
dist = [inf] * n
dist[0] = -H
for _ in range(m):
    u,v,a,h = map(int, input().split())
    u, v = u-1, v -1
    AL[u].append((v,a,h))
pq = [(-H,0)]

w = 0
while pq:
    H, loc = heappop(pq)
    if H > dist[loc]: continue
    for i, ea, eh in AL[loc]:
        num_of_attack = eh // A - 1 if eh % A == 0 else eh // A
        w =  num_of_attack * ea
        if dist[loc] + w >= dist[i]: continue
        dist[i] = dist[loc] + w
        heappush(pq, (dist[i], i))
if dist[n-1] >= 0 :
    print("Oh no")
else:
    print(-dist[n-1])


