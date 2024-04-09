n=int(input())
lst = [int(i) for i in input().split()]
sum = 0
res = []
for i in range(n):
    inp = lst[i]
    if inp != 0:
        res.append(inp)
    sum += inp * len(res)
largest = 0
curr = 0
for i in range(n-2,-1,-1):
    curr += res[i]
    if curr > largest:
        largest = curr
print(sum + largest)



def fluo(n, ls):
    output, big, val = 0, 0, 0
    new_ls = []
    counter = n-2
    # create a new list without the value 0
    for i in range(n):
        if ls[i] != 0:
            new_ls.append(ls[i])
        output += ls[i] * len(new_ls)
    # when you add values from the right of list, it kinda means you are shifting the values right.
    # what this means is that in your optimal solution you shift all values after the index of zero right by one.
    while counter >= 0:
        val += new_ls[counter]
        if val > big:
            big = val
        counter -= 1
    output = output + big
    return output

# print(fluo([1,0,-2]))
# print(fluo([0,-8,1,1,5]))
# print(fluo([2,-4,5,-3,0,-1,2]))