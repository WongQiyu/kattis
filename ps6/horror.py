from collections import deque
from math import inf

N,H,L = map(int,input().split())
horror_list = list(map(int,input().split()))

q = deque([horror_list])

HI = [inf] * N

for h in horror_list:
    HI[H] = 0

AL = [[] for _ in range(N)]: