import sys
inputs = sys.stdin.readline 

S = int(inputs())
constructor = 0

for i in range(1, S):
  if S == i + sum(list(map(int, list(str(i))))):
    constructor = i
    break

print(constructor)