import math

#def maxArea(self, height: List[int]) -> int:
def maxArea(height):
    marea = 0
    i, j = 0, len(height) - 1
    while i < j:
        if height[i] <= height[j]:
            area = height[i] * (j-i)
            i += 1
        else:
            area = height[j] * (j- i)
            j -= 1
        marea = max(area, marea)
    return marea
# print(maxArea([1,8,6,2,5,4,8,3,7]))
# print(maxArea([1,1]))

#contains duplicate
def containsDuplicate(nums) -> bool:
    res = set()
    for item in nums:
        if item in res:
            return True
        res.add(item)
    return False
#return len(set(nums)) != len(nums)

#majority element
def majorityElement(nums):
    res, count = 0, 0
    for n in nums:
        if count == 0:
            res = n
        count += (1 if n == res else -1)
    return res


#product except self
def productExceptSelf(nums):
    pfwd = 1
    res = []
    for val in nums:
        res.append(pfwd)
        pfwd *= val
    pbck = 1
    for i in range(len(nums)-1,0,-1):
        pbck *= nums[i]
        res[i-1] *= pbck
    return res
# print(productExceptSelf([1,2,3,4]))
# print(productExceptSelf([-1,1,0,-3,3]))

#interval
# insert interval- do not return append
def insert(intervals, newInterval):
    res = []
    for i, interval in enumerate(intervals):
        if newInterval[1] < interval[0]:
            res.append(newInterval)
            return res + intervals[i:]
        elif newInterval[0] > interval[1]:
            res.append(interval)
        else:
            newInterval = [min(interval[0],newInterval[0]), max(interval[1],newInterval[1])]
    res.append(newInterval)
    return res
# print(insert([[1,3],[6,9]],[2,5]))
# print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
# print(insert([],[2,5]))
# print(insert([[1,5]],[2,3]))

def merge(intervals):
    intervals.sort()
    res = [intervals[0]]
    for i in range(1,len(intervals)):
        if res[-1][1] >= intervals[i][0]:
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            res.append(intervals[i])
    return res


#sort colors - we use quicksort, 3 pointer
def sortColors(nums):
    def swap(i,j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
    i, l, r = 0, 0, len(nums) - 1
    # note <=
    while i <= r:
        if nums[i] == 0:
            swap(l,i)
            l += 1
            # we can increment i because whatever is before left pointer should be 0
        elif nums[i] == 2:
            swap(i,r)
            r -= 1
            i-= 1
            # we do not increment i because need to check if aft swap, i is 0
        i += 1
    return nums

print(sortColors([2,0,2,1,1,0]))

def maxProfit(prices):
    mini = math.inf
    profit = 0
    for val in prices:
        if val < mini:
            mini = val
        profit = max(profit,val-mini)
    return profit

def combinationSum(candidates, target):
    res = []
    def dfs(i,cur,total):
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target:
            return
        cur.append(candidates[i])
        dfs(i,cur,total+candidates[i])
        cur.pop()
        dfs(i + 1,cur, total)
    dfs(0,[],0)

#3sum leetcode
def threeSum(nums):
    res = []
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        l, r = i + 1, len(nums) -1
        while l <r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a,nums[l],nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return res

#/bin/bash
#^C for sth new