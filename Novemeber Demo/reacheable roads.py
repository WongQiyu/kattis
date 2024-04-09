# 2
# 5
# 3
# 0 1
# 1 2
# 3 4
# 2
# 1
# 0 1
def dfs(u):
    visited[u] = True
    for v in AL[u]:
        if visited[v]: continue
        dfs(v)
for _ in range(int(input())):
    v = int(input())
    n = int(input())
    AL = [[] for _ in range(v)]
    for _ in range(n):
        u,w = map(int, input().split())
        AL[u].append(w)
        AL[w].append(u)
    visited = [False] * v
    cc = 0
    for item in range(v):
        if not visited[item]:
            cc += 1
        dfs(item)
    print(cc - 1)



