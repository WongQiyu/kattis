
def count_sort(lst, sf):
    n = len(lst)
    res = [0 for _ in range(n)]
    count = [0 for _ in range(10)]

    for i in range(n):
        idx = lst[i] //sf
        count[idx % 10] += 1
    print(sf, count)
    for i in range(1,10):
        count[i] += count[i-1]

    for i in range(n-1,-1,-1):
        idx = lst[i] // sf
        # if sf == 10 or sf == 1:
        #     print(res[count[idx % 10] -1],idx,lst[i])
        res[count[idx % 10] -1] = lst[i]
        count[idx % 10] -= 1

    for i in range(n):
        lst[i] = res[i]
    print(sf, count, res)
def radix(lst):
    max_e = max(lst)
    sf = 1
    while max_e // sf > 0:
        count_sort(lst,sf)
        sf *= 10

data = [121, 432, 564, 23, 1, 45, 788,1]
#data = [12, 32, 64, 23, 1, 45, 78,1]
#radix(data)
count_sort(data)
print(data)