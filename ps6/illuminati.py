
n = int(input())

d = [[] for _ in range(n)]
res = 0
for i in range(n):
    ref = list(map(int, input().split()))[i+1:]
    for count, val in enumerate(ref):
        if val == 1:
            d[i].append(count+ i+1)
for val in d:
    for k in range(0,len(val)):
        compare_a = set(val[k+1:])
        compare_b = set(d[val[k]])
        res += len(compare_a & compare_b)
print(res)

