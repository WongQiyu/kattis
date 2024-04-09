
import bisect
def merge_sort(lst):
    n = len(lst)
    if n == 1:
        return lst

    mid = n//2
    l = lst[:mid]
    r = lst[mid:]
    merge_sort(l)
    merge_sort(r)

    a = b = c = 0
    while a < len(l) and b < len(r):
        if l[a] <= r[b]:
            lst[c] = l[a]
            a += 1
        else:
            lst[c] = r[b]
            b += 1
        c += 1
    while a < len(l):
        lst[c] = l[a]
        c += 1
        a += 1
    while b < len(r):
        lst[c] = r[b]
        c += 1
        b += 1

n =  int(input())
inp = list(map(int,input().split()))
merge_sort(inp)

q = int(input())
for _ in range(q):
    l, h = map(int, input().split())
    print(bisect.bisect_right(inp,h)-bisect.bisect_left(inp,l))



