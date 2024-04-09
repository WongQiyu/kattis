stat = [[0,0,0],[0,0,0]]
num = [0,0]
for _ in range(int(input())):
    line = input()
    id = 1 if line[0] == 'Y' else 0
    num[id] += 1
    for i in range(3):
        stat[id][i] += 1 if line[i+1] == 'Y' else 0
for i in range(3):
    inf_rate_non_vac = stat[0][i]/num[0]
    inf_rate_vac = stat[1][i] / num[1]
    if inf_rate_vac >= inf_rate_non_vac:
        print("Not Effective")
    else:
        print(100 * (inf_rate_non_vac-inf_rate_vac)/inf_rate_non_vac)
# https://open.kattis.com/submissions/9574480