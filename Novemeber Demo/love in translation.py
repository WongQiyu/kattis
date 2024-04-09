from heapq import heappush, heappop
from math import inf
from collections import defaultdict
n,m = map(int, input().split())
lang = set(input().split())
dist = dict(zip(lang,[inf] * n))
step = dict(zip(lang,[inf] * n))

lang.add('English')
AL = {key: [] for key in lang}
for _ in range(m):
    u,v,w = input().split()
    w = int(w)
    AL[u].append((v,w))
    AL[v].append((u,w))
pq = [(0,0,'English')]
dist['English'] = 0
step['English'] = inf

while pq:
    s, d, u1 = heappop(pq)
    if s > step[u1] or d > dist[u1]: continue
    for v1, w1 in AL[u1]:
        s1 = s + 1
        if s1 >= step[v1] or w1 >= dist[v1]: continue
        step[v1] = s1
        dist[v1] = w1
        heappush(pq, (step[v1], dist[v1], v1))

if sum(dist.values()) == inf:
    print('Impossible')
else:
    print(sum(dist.values()) )