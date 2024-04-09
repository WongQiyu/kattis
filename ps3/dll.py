class Vertex:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None
        self.partner = None


class DLL:
    def __init__(self):
        self._item = None
        self._head = None
        self._tail = None

    def append_pair(self,a,b):
        a = Vertex(a)
        b = Vertex(b)
        a.partner = b
        b.partner = a
        self.append(a)
        self.append(b)

    def append(self, vtx):
        if self._head is None:
            self._head = vtx
            self._tail = self._head
            self._item = self._head
        else:
            self._tail.next = vtx
            vtx.prev = self._tail
            vtx.next = None
            self._tail = vtx

    def traverse_f(self):
        if self._item.prev is not None:
            self._item = self._item.prev

    def traverse_b(self):
        if self._item.next is not None:
            self._item = self._item.next

    def remove_curr_node(self):
        tmp = self._item
        flag = True
        if tmp == self._head:
            self._head = tmp.next
            self._head.prev = None
            self._item = self._head
        elif self._item != self._tail:
            tmp.prev.next = tmp.next
            tmp.next.prev = tmp.prev
            self._item = tmp.next
        else:
            self._item = self._head
            flag = False
        return tmp, flag

    def traverse_r(self):
        node, flag = self.remove_curr_node()
        if flag:
            self.append(node)

    def traverse_c(self):
        if self._item.prev is not None and self._item.prev == self._item.partner:
            self._item = self._item.next if self._item is not self._tail else self._head
        else:
            curr_ele, flag = self.remove_curr_node()
            if curr_ele.partner == self._tail:
                self.append(curr_ele)
            else:
                if not flag:
                    self._tail = self._tail.prev
                    self._tail.next = None
                curr_ele.next = curr_ele.partner.next
                curr_ele.next.prev = curr_ele
                curr_ele.prev = curr_ele.partner
                curr_ele.partner.next = curr_ele

    def traverse_print(self):
        current_ele = self._head
        while current_ele:
            print(current_ele.item)
            current_ele = current_ele.next

    def get_curr(self):
        return self._item

n, instr = map(int, input().split())
l = DLL()
for _ in range(n):
    a, b = input().split()
    l.append_pair(a,b)
instr_set = list(input())
for item in instr_set:
    if item == 'P':
        print(l.get_curr().partner.item)
    if item == 'F':
        l.traverse_f()
    if item == 'B':
        l.traverse_b()
    if item == 'C':
        l.traverse_c()
    if item == 'R':
        l.traverse_r()

print()
l.traverse_print()
