import bisect


#print(count_consecutive_pairs(6, 20))
#print(count_consecutive_pairs(21, 20))

def find_longest_distance(blocks):
    n = len(blocks)
    result = 0
    for i in range(n):
        j = i
        while j > 0 and blocks[j - 1] >= blocks[j]:
            j -= 1
        low = j
        j = i
        while j < n - 1 and blocks[j + 1] >= blocks[j]:
            j += 1
        high = j
        result = max(result, high - low)
    return result + 1
print(find_longest_distance([2,6,8,5]))
print(find_longest_distance([1,5,5,2,6]))
print(find_longest_distance([1,1]))


import collections
def solution(K, A):
    m, n = len(A), len(A[0])
    count = [[0 for _ in range(n)] for _ in range(m)]
    house_count = 0
    house_coordinates = set()
    res = 0

    for i in range(m):
        for j in range(n):
            if A[i][j] == 1:
                bfs(A, i, j, K, count)
                house_count += 1
                house_coordinates.add((i, j))

    for i in range(m):
        for j in range(n):
            if count[i][j] == house_count and (i, j) not in house_coordinates:
                res += 1

    return res



def bfs(A, i, j, k, count):
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    q = collections.deque([(i, j, k)])
    visited = set()

    while len(q) != 0:
        for _ in range(len(q)):
            i, j, k = q.popleft()

            if (i, j) not in visited:
                visited.add((i, j))
                count[i][j] += 1

            for direction in directions:
                new_i, new_j, new_k = i + direction[0], j + direction[1], k - 1

                if 0 <= new_i < len(A) and 0 <= new_j < len(A[0]) and new_k >= 0 and (new_i, new_j) not in visited:
                    q.append((new_i, new_j, k - 1))

from math import sqrt

def count_consecutive_integer_products(A, B):
    count = 0
    sqrt_B = int(sqrt(B))
    for x in range(int(sqrt(A)), sqrt_B+1):
        product = x*(x+1)
        if A <= product <= B:
            count += 1
    return count



