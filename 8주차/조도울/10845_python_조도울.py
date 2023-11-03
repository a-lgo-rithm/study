import sys

inputs = sys.stdin.readline 

N = int(inputs())
queue = []
count = 0

for _ in range(N):
  command = list(inputs().split())

  if command[0] == "push":
    queue.append(int(command[1]))
    count += 1
  elif command[0] == "pop":
    if count != 0:
      print(queue[0])
      del(queue[0])
      count -= 1
    else:
      print(-1)
  elif command[0] == "size":
    print(count)
  elif command[0] == "empty":
    if count == 0: print(1)
    else: print(0)
  elif command[0] == "front":
    if count == 0: print(-1)
    else: print(queue[0])
  elif command[0] == "back":
    if count == 0: print(-1)
    else: print(queue[count - 1])