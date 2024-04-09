import collections
from collections import deque
def solution(K, A):
    # Implement your solution here
    m, n = len(A), len(A[0])
    c = [[0 for _ in range(n)] for _ in range(m)]
    res = 0
    num_house = 0
    xy_house = set() 
    for i in range(m):
        for j in range(n):
            if A[i][j] == 1:
                bfs(A, i, j, K, c)
                num_house += 1
                xy_house.add((i, j))
    for i in range(m):
        for j in range(n):
            if c[i][j] == num_house and (i, j) not in xy_house:
                res += 1
    return res


def bfs(A, i, j, k, c):
    dir = ((0, 1), (1, 0), (0, -1), (-1, 0))
    q = deque([(i, j, k)])
    vis = set()
    while q:
        for _ in range(len(q)):
            i, j, k = q.popleft()
            if (i, j) not in vis:
                vis.add((i, j))
                c[i][j] += 1
            for d in dir:
                new_i, new_j, new_k = i + d[0], j + d[1], k - 1
                if 0 <= new_i < len(A) and 0 <= new_j < len(A[0]) and new_k >= 0 and (new_i, new_j) not in vis:
                    q.append((new_i, new_j, k - 1))
def solution1(blocks):
    final = 0
    n = len(blocks)
    for i in range(n):
        l_check, r_check = i,i
        while  l_check > 0 and blocks[ l_check - 1] >= blocks[ l_check]:
            l_check -= 1
        l =  l_check

        while r_check < n - 1 and blocks[r_check + 1] >= blocks[r_check]:
            r_check += 1
        h = r_check
        final = max(final, h - l)
    return final + 1

    # n = len(blocks)
    # res = 0
    # for i in range(n):
    #     j = i
    #     while j > 0 and blocks[j - 1] >= blocks[j]:
    #         j -= 1
    #     low = j
    #     j = i
    #     while j < n - 1 and blocks[j + 1] >= blocks[j]:
    #         j += 1
    #     high = j
    #     res = max(res, high - low)
    # return res + 1

print(solution1([2,6,8,5]))
print(solution1([1,5,5,2,6]))
print(solution1([1,1]))