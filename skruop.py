#skruop
# n = int(input())
# volume = 7
# for _ in range(n):
#     if input() == "Skru op!":
#         if volume < 10:
#             volume += 1
#     else:
#         volume = max(volume -1, 0)
# print(volume)

#basic prog
l = input()
n, t = int(l.split()[0]), int(l.split()[1])
l2 = input()
a = [int(i) for i in l2.split()]
if t == 1:
    print(7)

elif t == 2:
    if a[0] > a[1]:
        print('Bigger')
    elif a[0] == a[1]:
        print('Equal')
    else:
        print('Smaller')
elif t == 3:
    print(sorted(a[:3])[1])

elif t == 4:
    print(sum(a))

elif t == 5:
    print(sum(list(filter(lambda x: x %2 == 0,a))))

elif t == 6:
    print(''.join([chr(i % 26 + 97) for i in a]))

elif t == 7:
    i = 0
    visited = set()
    while i < n:
        i = a[i]
        if i >= n:
            print('Out')
            break
        if i == n - 1:
            print('Done')
            break
        if i in visited:
            print('Cyclic')
            break
        visited.add(i)

from math import inf, ceil

pa, ka, pb, kb, n = map(int, input().split())
opt_a, opt_b, opt_c = inf, inf, inf
for ta in range(n // ka + 2):
    #for tb in range(n // kb + 2):
    tb = ceil((n - ta * ka) / kb)
    if ta * ka + tb *kb >=n:
            if ta * pa + tb * pb < opt_c:
                opt_a, opt_b, opt_c = ta, tb, ta * pa + tb * pb
print(opt_a, opt_b, opt_c)

h, p = map(int, input().split())

5 + 60 * h *1 * p / 100000

60 + 11* h *1 * p / 100000