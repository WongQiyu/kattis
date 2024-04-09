class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
class SLL:
    def __init__(self):
        self._head = None
        self._tail = None

    def appendleft(self, v):
        vtx = ListNode(v)
        vtx.next = self._head
        if self._head == None: self._tail = vtx
        self._head = vtx

    def append(self, v):
        if self._head == None:  # an important corner case
            self.appendleft(v)
        else:
            vtx = ListNode(v)
            self._tail.next = vtx
            self._tail = vtx

    def list_to_sll(self,arr):
        for item in arr:
            self.append(item)
    #circular
    def rotateRight(self, arr, k):
        head = self.list_to_sll(arr)
        if not head:
            return None
        last_ele = head
        length = 1
        while last_ele.next:
            last_ele = last_ele.next
            length += 1
        k = k % length
        last_ele.next = head
        temp_node = head

