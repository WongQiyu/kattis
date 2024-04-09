from heapq import heapify, heappop, heappush
n, k = map(int, input().split())
ls = []
for _ in range(n):
    ls.append(int(input()))
ls.sort()
pq = []
d = {}

for i in range(min(n,k)):
    heappush(pq,(ls[i],i))


people_left, result = n, 0
while people_left > 0:
    tmp = heappop(pq)
    result = tmp[0]
    car = tmp[1]
    if d.get(car,0) == 0:
        people_left -= 5
    else:
        people_left -= 4
    d[car] = d.get(car, 0) + 1
    heappush(pq, (ls[car] + d[car] * 2 * ls[car], car))

print(result)