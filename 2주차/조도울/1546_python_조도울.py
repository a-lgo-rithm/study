import sys

N = int(sys.stdin.readline())
numList = list(map(int,sys.stdin.readline().split()))

maxNum = max(numList)
sumNum = 0

for i in numList:
  sumNum += i / maxNum * 100

print(sumNum / N)