def search(nums,target):
    l,u = 0, len(nums) -1
    while l <= u:
        m = l + (u -l)//2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            u = m -1
    return -1

# def isBadversion(n):
#     return bisect_left(range(n), True, 1, key=isBadVersion)
def firstBadVersion(n):
    def isBadVersion(k):
        pass
    l,r,final = 1, n, 1
    while l <= r:
        m = l + (r-l) //2
        if isBadVersion(m) == False:
            l = m + 1
        else:
            r = m -1
            final = m
        return final

class Solution:
    def search(self,nums, target) :
        def get_search (lst, int1, low, high):
            if low > high:
                return -1
            else:
                mid = low + (high - low) // 2
                low1, mid1, high1 = lst[low], lst[mid], lst[high]
                if mid1 == int1:
                    return mid
                elif low1 <= mid1:
                    if (int1 <= mid1 and int1 >= low1):
                        return get_search(lst,int1, low, mid - 1)
                    return get_search(lst,int1, mid + 1, high)
                else:
                    if (int1 >= mid1 and int1 <= high1):
                        return get_search(lst,int1, mid + 1, high)
                    return get_search(lst,int1, low, mid - 1)
        return get_search(nums, target, 0, len(nums) -1)


