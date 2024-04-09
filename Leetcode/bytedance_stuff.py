#array
import bisect
def productExceptSelf(nums):
    res = [1 for _ in range(len(nums))]
    for i in range(1, len(nums)):
        res[i] = res[i - 1] * nums[i - 1]
        # [1,1,2,6]
    right = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res

def lengthOfLIS(nums):
    res = []
    for x in nums:
        if len(res) == 0 or res[-1] < x:
            res.append(x)
        else:
            idx = bisect.bisect_left(res,x)
            res[idx] = x

    return len(res)



#tbc
def numSubseq(nums, target):
    nums.sort()
    possible = 0
    n = len(nums)
    i = 0
    while i < n and nums[i] <= target:
        min_val = nums[i]
        j = i
        while j < n and nums[j] + min_val <= target:
            possible += 1
            j += 1
        i += 1
    return possible

#string
def longestValidParentheses(s):
    ans,stack = 0 , [-1]
    for i, c in enumerate(s):
        if c == ")":
            # if you pop for ) it is False as [] if ( pop will not be empty list
            stack.pop()
            if stack:
                ans = max(ans, i -stack[-1])
                continue
        stack.append(i)
    return ans


