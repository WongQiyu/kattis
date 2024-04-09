import sys

a,b = map(int,input().split())
max_val = a * (a-1) //2
min_val = a -1
if b > max_val or b < min_val:
    print(-1)
    sys.exit()
count = 0
distinct = set()
gap = 1
res = []

while count < b and gap <= a - 1:
    for i in range(1, a + 1):
        j = i + gap
        if j > a or count >=b:
            break
        sum = i + j
        if sum not in distinct:
            distinct.add(sum)
            res.append((i,j))
            count += 1
    gap += 1
if len(res) < b:
    print(-1)
else:
    for item in res:
        print(item[0],item[1])






