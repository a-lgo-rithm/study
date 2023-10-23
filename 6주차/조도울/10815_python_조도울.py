import sys
inputs = sys.stdin.readline 

N = int(inputs())
numberCard = set(map(int, inputs().split()))
M = int(inputs())
existCheck = map(int, inputs().split())

for i in existCheck:
  if i in numberCard: print("1", end=" ")
  else: print("0", end=" ")