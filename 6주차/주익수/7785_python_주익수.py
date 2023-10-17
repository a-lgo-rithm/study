import sys

n = int(sys.stdin.readline().rstrip())

human = set()

for i in range(n):
    name, io = map(str, sys.stdin.readline().split())
    if io == 'enter':
        human.add(name)
    else:
        human.remove(name)

human = sorted(list(human), reverse=True)
for i in human:
    print(i)
