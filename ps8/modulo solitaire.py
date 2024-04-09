import sys
from collections import deque
m, n, s = map(int, input().split())
sys.setrecursionlimit(10000000)

el = deque()
vis = {s}

q = deque([[s,0]])

for _ in range(n):
    a,b =  map(int, input().split())
    el.append((a,b))


while q:
    checker = q.popleft()
    s1, level = checker[0], checker[1]
    for i,j in el:
        res = (s1 * i + j) % m
        if res == 0:
            print(level + 1)
            sys.exit()
        if res in vis:
            continue
        vis.add(res)
        q.append([res, level+ 1])

print(-1)


