from collections import deque

C,P,X,L = map(int, input().split())
X, L = X-1, L-1

AL = [[] for _ in range(C)]

deg = [0] * C

for _ in range(P):
    A, B = map(lambda x: int(x) -1 , input().split())
    AL[A].append(B)
    deg[B] += 1
    AL[B].append(A)
    deg[A] += 1

ori_deg = [deg[i] for i in range(C)]

q = deque([L])
leave = [False] * C
while q:
    u= q.popleft()
    leave[u] = True
    for v in AL[u]:
        if leave[v]: continue
        deg[v] -= 1
        if  2 * deg[v] <= ori_deg[v]:
            q.append(v)
print("stay" if not leave[X] else 'leave')