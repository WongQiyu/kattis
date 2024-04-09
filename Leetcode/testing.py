from collections import deque
n = int(input())
for _ in range(n):
    m = int(input())
    if m < 2:
        print('No')
    else:
        val = deque(list(map(int,input().split())))
        left, right = val.popleft(), val.pop()
        while val:
            print(left,right)
            new_left = val.popleft()
            if val:
                new_right = val.pop()
            else:
                new_right = new_left
            if min(left, right) < min(new_left, new_right) and max(left, right) < max(new_left, new_right):
                print('No')
                val = []
            left,right = new_left,new_right
        print('Yes')
