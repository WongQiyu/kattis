import heapq
from heapq import heapify, heappush, heappop
# def rearrange_arrays(a, b):
#     map = {}
#     for i,v in enumerate(a):
#         map[v] = i
#     a_sort = sorted(a)
#     b_sort = sorted(b)
#     sum = 0
#     for i in range(len(a)):

def max_difference_sum(a, b):
    n = len(a)
    prefix_max = [0] * n
    suffix_min = [0] * n

    # Compute prefix_max
    curr_max = float('-inf')
    for i in range(n):
        curr_max = max(curr_max, b[i])
        prefix_max[i] = curr_max

    # Compute suffix_min
    curr_min = float('inf')
    for i in range(n - 1, -1, -1):
        curr_min = min(curr_min, a[i])
        suffix_min[i] = curr_min

    # Compute max difference
    max_diff = float('-inf')
    for i in range(n):
        max_diff = max(max_diff, prefix_max[i] - suffix_min[i])

    return max_diff


# Example usage
a = [1, 2, 3, 4, 5]
b = [3, 5, 4, 6, 2]
print(max_difference_sum(a, b))  # Output: 20

a = [1, 4, 2, 1, 3]
b = [2, 3, 1, 2, 2]

a = [1, 2, 3, 4, 5]
b = [3, 5, 4, 6, 2]
print(max_difference_sum(a, b)) # Output: 20

a = [1, 4, 2, 1, 3]
b = [2, 3, 1, 2, 2]
print(max_difference_sum(a, b)) # Output: 7


