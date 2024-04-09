# def spiralOrderOld(matrix):
#     n = len(matrix) #3
#     m = len(matrix[0]) #4
#     res = []
#     def helper(res,i):
#         for k in range(i,m-i):
#             res.append(matrix[i][k])
#         for k in range(i+1,n-i):
#             res.append(matrix[k][-(i+1)])
#         for k in range(m-i-2,i-1,-1):
#             res.append(matrix[n-i-1][k])
#         for k in range(n-i-2,i,-1):
#             res.append(matrix[k][i])
#     for p in range(0,n-1):
#         helper(res,p)
#     return res
import bisect
def spiralOrder(matrix):
   l,r,t,b = 0,len(matrix[0]), 0,len(matrix)
   res = []
   while l < r and t < b:
       for i in range(l,r):
           res.append(matrix[t][i])
       t += 1
       for i in range(t,b):
           res.append(matrix[i][r-1])
       r -= 1
       if not (l < r and t < b): break
       for i in range(r -1,l-1,-1):
           res.append(matrix[b-1][i])
       b -= 1
       for i in range(b-1,t-1, -1):
           res.append(matrix[i][l])
       l += 1
   return res
print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
#[1,2,3,4,8,12,11,10,9,5,6,7]


class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        val = self.store.get(key,[])
        l,r = 0, len(val) -1
        while l <= r:
            m = l + (r-l)//2
            if val[m][1] <= timestamp:
                res = val[m][0]
                l = m + 1
            else:
                r = m-1
        return res

def climbStairs(n):
    one, two = 1, 1
    for i in range(n-1):
        temp = one
        one = one + two
        two = temp
    return one

def jobScheduling(startTime, endTime, profit):
    combine = list(zip(startTime, endTime, profit))
    #combine.sort()
    #startTime.sort()
    def checker(i):
        while combine[i][1] < combine[j][0]:
            optimal = max()

