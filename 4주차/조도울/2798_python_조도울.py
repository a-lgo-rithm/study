import sys
inputs = sys.stdin.readline 

N, M = map(int, inputs().split())
numList = list(map(int, inputs().split()))
numList.sort()
correctNumber = 0

for i in range(N - 2):
  for j in range(i+1, N - 1):
    for k in range(j + 1, N):
      qNum = numList[i] + numList[j] + numList[k]
      if M < qNum: break
      elif correctNumber < qNum: correctNumber = qNum 
print(correctNumber)