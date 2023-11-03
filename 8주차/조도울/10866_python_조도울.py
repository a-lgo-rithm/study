import sys

inputs = sys.stdin.readline 

N = int(inputs())
deque = []
count = 0

for _ in range(N):
  command = list(inputs().split())

  if command[0] == "push_front":
    deque = [int(command[1])] + deque
    count += 1
  elif command[0] == "push_back":
    deque.append(int(command[1]))
    count += 1
  elif command[0] == "pop_front":
    if count != 0:
      print(deque[0])
      del(deque[0]) 
      count -= 1
    else:
      print(-1)
  elif command[0] == "pop_back":
    if count != 0:
      print(deque[count-1])
      del(deque[count-1])
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
    else: print(deque[0])
  elif command[0] == "back":
    if count == 0: print(-1)
    else: print(deque[count-1])