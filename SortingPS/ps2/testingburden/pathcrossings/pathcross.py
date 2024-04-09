#!/usr/bin/python3
import math


def get_distance(lst_a, lst_b):
    return math.dist(lst_a, lst_b) <= 1000


def new_res(a, b):
    if a < b:
        return (a, b)
    return (b, a)


def merge_sort_key(a, key):
    n = len(a)
    if n == 1 or n == 0:
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
    return a


p, n = map(int, input().split())
lst = []

for _ in range(n):
    obj = [int(i) for i in input().split()]
    lst.append(obj)

merge_sort_key(lst, 3)

out = set()

for i in range(n - 1):
    timing = lst[i][3]
    j = i + 1
    while j < min(i + 5, n) and lst[j][3] <= timing + 10:
        res_val = new_res(lst[i][0], lst[j][0])
        if lst[i][0] != lst[j][0] and res_val not in out:
            if get_distance([lst[i][1], lst[i][2]], [lst[j][1], lst[j][2]]):
                out.add(res_val)
        j += 1


print(len(out))
if len(out) != 0:
    res = merge_sort_key(list(out), None)
    for item in res:
        print(item[0], item[1])

    # for item in res:
    #     ai, bi = map(int, item.split())
    #     print(ai,bi)
    # print(item[0],item[2])
    # print(int(item[0]), int(item[2]))

# def new_res(a,b):
#     if a < b:
#         res = f'{a} {b}'
#     else:
#         res = f'{b} {a}'
#     return res
#
# def bin_search_key(lst,obj,key):
#     low = 0
#     high = len(lst) - 1
#     while low <= high:
#         mid = (low + high) //2
#         if lst[mid][key] == obj[key]:
#             return mid
#         elif lst[mid][key] > obj[key]:
#             high = mid -1
#         else:
#             low = mid + 1
#     return low
#
#
# p, n = map(int, input().split())
# lst = [[int(i) for i in input().split()]]
#
# for _ in range(n-1):
#     obj = [int(i) for i in input().split()]
#     idx = bin_search_key(lst, obj, 3)
#     lst.insert(idx,obj)
#
# out = set()
# max_out = 4950
# res = []
# for i in range(n -1):
#     if len(out) > max_out:
#         break
#     timing = lst[i][3]
#     j = i + 1
#     while j < min(i + 5,n) and lst[j][3] <= timing + 10 and len(out) <= 4950 :
#         res_val = new_res(lst[i][0], lst[j][0])
#         if lst[i][0] != lst[j][0] and res_val not in out :
#             if euclidean_dist_check(lst[i][1],lst[i][2], lst[j][1],lst[j][2]):
#                 out.add(res_val)
#                 bisect.insort(res,res_val)
#         j += 1
#
# print(len(out))
# #out = sorted(out)
# print('\n'.join(res))
# def merge_sort(a):
#     n = len(a)
#     if n == 1:
#         return a
#     mid = n//2
#     left = a[:mid]
#     right = a[mid:]
#     merge_sort(left)
#     merge_sort_key(right)
#     i = j = k = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             a[k] = left[i]
#             i += 1
#         else:
#             a[k] = right[j]
#             j += 1
#         k += 1
#     while i < len(left):
#         a[k] = left[i]
#         k += 1
#         i += 1
#     while j < len(right):
#         a[k] = right[j]
#         k += 1
#         j += 1
#     return a

# for i in range(n -1):
#     timing = lst[i][3]
#     j = i + 1
#     while j < min(i + 5,n) and lst[j][3] <= timing + 10:
#         key = min (lst[i][0], lst[j][0])
#         val = max (lst[i][0], lst[j][0])
#         if key != val and val not in out.get(key,{}) :
#             if get_distance([lst[i][1],lst[i][2]], [lst[j][1],lst[j][2]]):
#                 out.get(key,{}).append(val)
#         j += 1
# def euclidean_dist_check(x1,y1,x2,y2):
#     return math.sqrt((x1 - x2) ** 2 + (y1 - y2) **2) <= 1000
# p, n = map(int, input().split())
# check = [[] for _ in range(p)]
#
# for _ in range(n):
#     inp = input()
#     k,v = int(inp.split()[0]), list(map(int, inp.split()[1:]))
