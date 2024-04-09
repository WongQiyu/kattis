n = int(input())
lst = []
for _ in range(n):
    inp = tuple(map(int, input().split()))
    lst.append(inp)
lst.sort(key = lambda x: x[1])
finish = 0
count = 0
for item in lst:
    if finish <= item[0]:
        finish = item[1]
        count += 1
print(count)