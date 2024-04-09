import bisect

import math


def get_distance(lst_a, lst_b):
    return math.dist(lst_a, lst_b) <= 1000


def merge_sort_key(a, key):
    n = len(a)
    if n == 1:
        return a
    mid = n // 2
    left = a[:mid]
    right = a[mid:]
    merge_sort_key(left, key)
    merge_sort_key(right, key)
    i = j = k = 0
    while i < len(left) and j < len(right):
        check = left[i] <= right[j] if not key else left[i][key] <= right[j][key]
        if check:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        a[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        a[k] = right[j]
        k += 1
        j += 1


p, n = map(int, input().split())
check = [[] for _ in range(p)]
result = set()

for _ in range(n):
    inp = input()
    k,v = int(inp.split()[0]), list(map(int, inp.split()[1:]))
    check[k-1].append(v)

i, k = 0, -1

while i < p:
    if check[i] == []:
        i += 1
        continue
    if i < k:
        k = i
        merge_sort_key(check[i], 2)
    mid = len(check[i]-1) //2
    l,h = check[mid][2] - 10, check[mid][2] + 10
    low_idx = bisect.bisect_left(l, key = lambda x:x[2] )
    high_idx = bisect.bisect_right(h, key = lambda x:x[2] )
    cnt = high_idx - low_idx


