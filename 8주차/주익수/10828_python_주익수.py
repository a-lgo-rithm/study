import sys


class Stack:

    def __init__(self):
        self.list = []
        self.count = 0

    def push(self, x):
        self.list.append(x)
        self.count += 1

    def pop(self):
        if self.count == 0:
            print(-1)
        else:
            print(self.list.pop(-1))
            self.count -= 1

    def size(self):
        print(self.count)

    def empty(self):
        if self.count == 0:
            print(1)
        else:
            print(0)

    def top(self):
        if self.count == 0:
            print(-1)
        else:
            print(self.list[-1])


N = int(sys.stdin.readline().rstrip())

stack = Stack()
for i in range(N):
    console = list(map(str, sys.stdin.readline().rstrip().split()))

    if console[0] == 'push':
        stack.push(*console[1:])

    if console[0] == 'pop':
        stack.pop()

    if console[0] == 'size':
        stack.size()

    if console[0] == 'empty':
        stack.empty()

    if console[0] == 'top':
        stack.top()
