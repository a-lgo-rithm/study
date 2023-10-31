import sys


class Deque:

    def __init__(self):
        self.list = list()
        self.count = 0

    def push_front(self, x):
        self.list.insert(0, x)
        self.count += 1

    def push_back(self, x):
        self.list.append(x)
        self.count += 1

    def pop_front(self):
        if self.count == 0:
            print(-1)
        else:
            print(self.list.pop(0))
            self.count -= 1

    def pop_back(self):
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

deque = Deque()
for i in range(N):
    console = list(map(str, sys.stdin.readline().rstrip().split()))

    if console[0] == 'push_front':
        deque.push_front(*console[1:])

    if console[0] == 'push_back':
        deque.push_back(*console[1:])

    if console[0] == 'pop_front':
        deque.pop_front()

    if console[0] == 'pop_back':
        deque.pop_back()

    if console[0] == 'size':
        deque.size()

    if console[0] == 'empty':
        deque.empty()

    if console[0] == 'front':
        deque.front()

    if console[0] == 'back':
        deque.back()
