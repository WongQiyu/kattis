#all copy solution
#invert binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
#balanced
class Solution:
    def isBalanced(self, root):
        def check(root):
            if root is None:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1:
                return -1
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1
            return max(left,right) + 1
        return check(root) != -1
#diameter
class Solution:
    def diameterOfBinaryTree(self, root):
        self.result = 0
        def count(root):
            if root is None:
                return 0
            left = count(root.left)
            right = count(root.right)
            self.result = max(self.result, left + right)
            return max(left,right) + 1
        count(root)
        return self.result

class Solution:
    def maxDepth(self, root):
        def check(root):
            if root:
                left = check(root.left)
                right = check(root.right)
                return 1 + max(left,right)
            return 0
        return check(root)
#level order - queue
from collections import deque
class Solution:
    def levelOrder(self, root):
        trav, q = [], deque([root])
        while q:
            level, num = [], len(q)
            for _ in range(num):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                trav.append(level)
        return trav
print(TreeNode(0,TreeNode(1),2).left.left)

#level order bfs
def levelOrder(root):
    ans = []
    def bfs(curr = root, level = 0):
        if len(ans) > level:
            ans[level].append(curr.val)
        else:
            ans.append([curr.val])
        bfs(curr.left,level + 1)
        bfs(curr.right, level + 1)
        return
    bfs()
    return ans



#LinkedList

#mergeTwoList
def mergeTwoLists(self,a,b):
    if not a or b and a.val > b.val:
        a,b = b, a
    if a:
        a.next = self.mergeTwoList(a.next,b)
    return a
def hasCycle(head):
    fast = slow = head
    while fast and slow:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
        return False
#reverse LL
def reverseList(head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev



