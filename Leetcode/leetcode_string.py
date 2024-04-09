def isPalindrome(s):
    l,r = 0, len(s) -1
    while l < r <= len(s) -1:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        else:
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
    return True
    # s = ''.join(e for e in s if e.isalnum()).lower()
    # return s == s[::-1]
# print(isPalindrome("A man, a plan, a canal: Panama"))
# print(isPalindrome("race a car"))
# print(isPalindrome(" "))

def isAnagram(s,t):
    memo = {}
    for item in s:
        memo[item] = memo.get(item,0) + 1
    for item in t:
        if item in memo:
            memo[item] -= 1
        else:
            return False
    return all(count == 0 for count in memo.values())

def longestPalindrome(s):
    memo = set()
    for token in s:
        memo.add(token) if token not in memo else memo.remove(token)
        # #try:
        #     memo.remove(token)
        # #except KeyError:
        #     memo.add(token)
    odd = len(memo) > 0
    return len(s) - len(memo) + 1 if odd else len(s)

def lengthOfLongestSubstring(s):
    memo = set()
    start, end, maxi = 0,0,0
    while start < len(s) and end < len(s):
        token = s[end]
        if token in memo:
            memo.remove(s[start])
            start += 1
        else:
            end += 1
            memo.add(token)
            maxi = max(maxi,len(memo))
    return maxi

def myAtoi(s):
    ans = index = 0
    MAX, MIN = 2147483647, -2147483648
    s = s.strip()
    if not s:
        return 0
    sign = -1 if s[0] == "-" else 1
    if s[0] in set("+-"):
        index += 1
    while index < len(s) and s[index].isdigit():
        ans = ans * 10 + int(s[index])
        index += 1
    ans *= sign
    ans = min(MAX,max(ans,MIN))
    return ans

def findAnagrams(s,p):
    i = 0
    n = len(p)
    res = []
    while i + n < len(s):
        if isAnagram(s[i:n],p):
            res.append(i)
        i += 1
    return res
print(findAnagrams("cbaebabacd","abc"))

#do this again
import collections
def minWindow(s,t):
    missing_counter = len(t)
    w_start = w_end = curr = 0
    memo = collections.Counter(t)

    for index,token in enumerate(s,1):
        if memo[token] > 0:
            missing_counter -= 1
        memo[token] -= 1
        if missing_counter == 0:
            while curr < index and memo[s[curr]] < 0:

    return s[w_start:w_end]
