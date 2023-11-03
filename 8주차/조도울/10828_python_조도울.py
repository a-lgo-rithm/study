import sys

inputs = sys.stdin.readline 

N = int(inputs())
stack = []
top = 0

for _ in range(N):
  command = list(inputs().split())

  if command[0] == "push":
    stack.append(int(command[1]))
    top += 1
  elif command[0] == "pop":
    if top != 0:
      print(stack[top-1])
      del(stack[top-1])
      top -= 1
    else:
      print(-1)
  elif command[0] == "size":
    print(top)
  elif command[0] == "empty":
    if top == 0: print(1)
    else: print(0)
  elif command[0] == "top":
    if top == 0: print(-1)
    else: print(stack[top-1])