from math import inf
from heapq import heappush,heappop
N, S, T = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(N)]

dist = [inf] * N
dist[S] = 0
pq = [(dist[S],S)]

while pq:
    d, u = heappop(pq)
    if D[u][v] == 0: continue
    for v in range(N):
        if d > dist[u]: continue
        if dist[u] + D[u][v] >= dist[v]: continue
        dist[v] = dist[u] + D[u][v]
        heappush(pq, (dist[v],v))
print(dist[T])