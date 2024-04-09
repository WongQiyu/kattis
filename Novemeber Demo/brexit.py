v, n, h, l = map(int,input().split())
AL = [[]for _ in range(v)]
checker = [False for _ in range(v)]
checker[l] = True
am = [[0 for _ in range(v) ] for _ in range(v)]
for _ in range(n):
    a, b = map(int,input().split())
    am[a][b] = 2 if a == 0 or b == 0 else 1
    am[b][a] = 2 if a == 0 or b == 0 else 1

    # AL[a].append(b)
    # AL[b].append(a)
for item in AL[l]:
    AL[item]
