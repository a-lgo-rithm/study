import sys


class Queue:

    def __init__(self):
        self.list = list()
        self.count = 0

    def push(self, x):
        self.list.append(x)
        self.count += 1

    def pop(self):
        if self.count == 0:
            print(-1)
        else:
            print(self.list.pop(0))
            self.count -= 1

    def size(self):
        print(self.count)

    def empty(self):
        if self.count == 0:
            print(1)
        else:
            print(0)

    def front(self):
        if self.count == 0:
            print(-1)
        else:
            print(self.list[0])

    def back(self):
        if self.count == 0:
            print(-1)
        else:
            print(self.list[-1])


N = int(sys.stdin.readline().rstrip())

queue = Queue()
for i in range(N):
    console = list(map(str, sys.stdin.readline().rstrip().split()))

    if console[0] == 'push':
        queue.push(*console[1:])

    if console[0] == 'pop':
        queue.pop()

    if console[0] == 'size':
        queue.size()

    if console[0] == 'empty':
        queue.empty()

    if console[0] == 'front':
        queue.front()

    if console[0] == 'back':
        queue.back()
