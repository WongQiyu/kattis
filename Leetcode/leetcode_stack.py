#all done myself

from collections import deque
def isValid(s):
    o = deque([])
    c = deque([])
    check = {'(':')','{':'}','[':']'}
    for item in s:
        if item in check:
            if bool(c) and check[item] != c.popleft():
                return False
            o.append(item)
        elif not bool(o):
            return False
        elif check[o.pop()] != item:
            return False

    return True if not bool(o) else False
print(isValid("()"))
print(isValid("(}"))

from collections import deque


class MyQueue:

    def __init__(self):
        self.stack = deque([])

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.popleft()

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return not bool(self.stack)

import heapq
from heapq import heapify, heappush, heappop
class MinStack:

    def __init__(self):
        self.stack = deque([])
        self.heap = []
        heapify(self.heap)
        self.mem = set()

    def push(self, val: int) -> None:
        self.stack.append(val)
        heappush(self.heap, val)

    def pop(self) -> None:
        a = self.stack.pop()
        self.mem.add(a)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        while self.heap[0] in self.mem:
            self.mem.remove(self.heap[0])
            heappop(self.heap)

        return self.heap[0]
import math
def evalRPN(tokens):
    ops = set(['+', '-', '*','/'])
    stack = []
    for item in tokens:
        if item in ops:
            b = stack.pop()
            a = stack.pop()
            # if item == '/':
            #     item = '//'
            stack.append(int(eval(f'{a}{item}{b}')))

        else:
            stack.append(int(item))
    return stack.pop()
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

