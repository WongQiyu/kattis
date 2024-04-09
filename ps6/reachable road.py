def dfs(u):
    vis[u] = True
    for v in AL[u]:
        if vis[v]: continue
        dfs(v)
for _ in range(int(input())) :
    V = int(input())
    E = int(input())
    AL = [[] for _ in range(V)]
    for _ in range(E):
        u,v = map(int, input().split())
        AL[u].append(v)
        AL[v].append(u)
    print(AL)
    numCC = 0
    vis = [False] * V
    for u in range(V):
        if not vis[u]:
            print(u)
            numCC += 1
        dfs(u)
    print(numCC -1)
