import math
from math import inf
#https://leetcode.com/problems/maximum-subarray/discuss/1595195/C%2B%2BPython-7-Simple-Solutions-w-Explanation-or-Brute-Force-%2B-DP-%2B-Kadane-%2B-Divide-and-Conquer
# memoization
def maxSubArray(nums):
    def solve(i,must_pick):
        if i >= len(nums): return 0 if must_pick else -inf
        return max(nums[i] + solve(i +1, True), 0) if must_pick else solve(i +1, False)
    return solve(0, False)

#dp -tabulation
def maxSubArray2(nums):
    dp = [*nums]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], nums[i] + dp[i-1])
    return max(dp)

def maxSubArray3(nums):
    cur_max, main_max = 0, -inf
    for c in nums:
        cur_max = max(c,cur_max + c)
        main_max = max(main_max,cur_max)
    return main_max

def maxSubArray4(nums):
    pre, suf = [*nums], [*nums]
    for i in range(1, len(nums)):
        pre[i] += max(0,pre[i-1])
        suf[i] += max(0, suf[i+1])
    def maxi(A,L,R):
        if L == R:
            return A[L]
        mid = (L + R) //2
        return max(maxi(A,L,mid),maxi(A,mid+1,R), pre[mid], suf[mid+1])
    return maxSubArray4(nums, 0, len(nums) -1)