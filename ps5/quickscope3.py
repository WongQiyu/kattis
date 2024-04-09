from collections import defaultdict
n = int(input())
pointer_dic = defaultdict(lambda: [])

big_d = [{}]
scope_ind = 0
res = []

def declare(inp):
    if inp[1] in big_d[-1]:
        return 'MULTIPLE DECLARATION'
    else:
        pointer_dic[inp[1]].append(scope_ind)
        big_d[-1][inp[1]] = inp[2]


def typeof(inp):
    if inp[1] in pointer_dic :
        return big_d[pointer_dic[inp[1]][-1]][inp[1]]
    else:
        return 'UNDECLARED'

def close():
    rem = big_d.pop()
    for item in rem:
        pointer_dic[item].pop()
        if not pointer_dic[item]:
            del pointer_dic[item]



for _ in range(n):
    inp = input().split()
    if inp[0] == 'DECLARE':
        tmp = declare(inp)
        if tmp == 'MULTIPLE DECLARATION':
            res.append(tmp)
            print()
            break
    elif inp[0] == 'TYPEOF':
        res.append(typeof(inp))
    elif inp[0] == '{':
        scope_ind = len(big_d)
        big_d.append({})
    else:
        scope_ind -= 1
        close()
for item in res:
    print(item)