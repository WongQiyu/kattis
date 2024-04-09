#S2 Papers
#12
def get_triplet(main,check,check_set,neg_main):
    for u in main:
        for v in check:
            if v > u:
                break
            if u - v in check_set:
                a,b = min(v, u-v),max (v, u-v)
                if not neg_main:
                    a,b = -a, -b
                else:
                    u = -u
                if (a,b,u) not in res:
                    res.add((a,b,u))
                    print((a,b,u))
l = [1,2,3,4,5,6,-7]
l.sort()
neg = [abs(i) for i in l if i < 0]
set_neg = set(neg)
pos = l[len(neg):]
set_pos = set(pos)
res = set()
get_triplet(neg, pos, set_pos,True)
get_triplet(pos, neg, set_neg,False)
if len(res) == 0:
    print("No such triple")

#13
from collections import deque
l = [8,1,2,3,4,5,8,6,7]
q = deque(l)
q_new = deque([q.popleft()])
while q:
    a = q_new.pop()
    b = q.popleft()
    if a == b:
        q_new.append(a)
        q_new.append(b)
    else:
        q_new.append(max(a,b))
print(q_new)

#14 O(N *D)
N = 10
D = 3
ncol = [-1,1,0,0]
norw = [0,0,-1,1]
AM = [['' for _ in range(N)] for _ in range(N)]
dead = dict()
EL = {'a': (0,0),'b':(6,3),'c': (6,4),'d':(3,6),'e':(2,1)}
q = deque([])
for k in EL.keys():
    a,b = EL[k]
    AM[a][b] = k
    tmp = deque([(a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)])
    EL[k] = tmp
for i in range(1,D):
   for kk,v in EL.items():
       if kk in dead:
           continue
       e,f,g,h = v
       if e[0]  < 0 or f[0]  >= N or g[1]  < 0 or h[1]  >= N:
           dead[kk] = i
       for things in (v):
           c,m = things
           if AM[c][m] != '':
               dead[AM[c][m]] = i
               dead[kk] = i
       if kk not in dead:
           EL[kk] = deque([(e[0] - 1, e[1]), (f[0] + 1, f[1]), (g[0], g[1] - 1), (h[0], h[1] + 1)])

for item in EL.keys():
    print(dead.get(item,'Alive'))
print(dead)





