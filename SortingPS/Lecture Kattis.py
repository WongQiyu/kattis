
#no thanks
n = int(input())
deck = sorted(list(map(int, input().split())))
score = deck[0]

for i in range(n-1):
    if deck[i] +1 != deck[i+1]:
        score += deck[i+1]
print(score)
# high ordering - insertion sort

for _ in range(int(input())):
    line  = list(map(int, input().split()))
    k, h = line[0], line[1:]
    ans = 0
    n = 20
    #print(h)
    for i in range(1,n):
        x = h[i]
        j = i - 1
        while (j >= 0) and (h[j] > x):
            h[j+1] = h[j]
            j -= 1
            ans += 1
        h[j+1] = x
    print(k,ans)


#mjehuric - bubble sort . this case is O(1)
n = 5
a = list(map(int, input().split()))
for i in range(n):
    for j in range(n -1):
        if a[j] > a[j +1]:
            a[j], a[j +1] = a[j+1], a[j]
            print(*a)
#sort of sorting
while True:
    n = int(input())
    if n == 0: break
    names = [input() for _ in range(n)]
    print()
    print(*sorted(names, key = lambda x: x[:2]), sep ="\n")
