from heapq import heappush, heappop
from math import inf
while True:
    n, m, q,s = map(int, input().split())
    if n + m + q + s == 0:
        break
    AL = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int,input().split())
        AL[u].append((v,w))
    dist = [inf] * n
    dist[s] = 0

    pq = [(0,s)]

    while pq:
        d, u = heappop(pq)
        if d > dist[u]: continue
        for v, w in AL[u]:
            if dist[u] + w >= dist[v]: continue
            dist[v] = dist[u] + w
            heappush(pq, (dist[v],v))
    for _ in range(q):
        t = int(input())
        print("Impossible" if dist[t] == inf else dist[t])
    print()