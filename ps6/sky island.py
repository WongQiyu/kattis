from collections import deque

N, M = map(int, input().split())
AL = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    AL[a].append(b)
    AL[b].append(a)
vis = [False] * N
q = deque([0])
vis[0] = True

while q:
    u = q.popleft()
    for v in AL[u]:
        if vis[v]: continue
        vis[v] = True
        q.append(v)
all_connected = True
for u in range(N):
    if not vis[u]:
        print('No')
        all_connected = False
        break
if all_connected:
    print("Yes")
