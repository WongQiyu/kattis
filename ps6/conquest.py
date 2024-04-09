from heapq import heappush, heappop
pq_heapq = []
n, m = map(int, input().split())
AL = [[] for _ in range(n)]
weight = []
for _ in range(m):
    u, v = map(int, input().split())
    u,v = u-1, v-1
    AL[u].append(v)
    AL[v].append(u)

for _ in range(n):
    weight.append(int(input()))
conquered = {0}
added = set()

curr = weight[0]
for val in AL[0]:
    heappush(pq_heapq,(weight[val], val))
    added.add(val)

while pq_heapq:
    tmp = heappop(pq_heapq)
    w, v = tmp[0], tmp[1]
    if w >= curr:
        break
    if v in conquered:
        continue
    conquered.add(v)
    curr += w
    for val in AL[v]:
        if val not in conquered and val not in added:
            heappush(pq_heapq, (weight[val], val))

print(curr)


