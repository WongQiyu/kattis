from collections import defaultdict
l, k, s = map(int, input().split())
d = defaultdict(lambda: [])

for _ in range(l):
    inp = input()
    i, t = int(inp.split()[0]), inp.split()[1]
    t = t.split('.')
    t = int(t[0]) * 60 + int(t[1])
    d[i].append(t)
d_new = {key:sum(value) for (key,value) in d.items() if len(value) == k}
for w in sorted(d_new.items(), key=lambda x: (x[1],x[0])):
    print(w[0])


