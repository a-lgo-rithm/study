import sys

N = int(sys.stdin.readline())
numList = list(map(int,sys.stdin.readline().split()))

maxNum = numList[0]
minNum = numList[0]

for i in numList[1:]:
  if i > maxNum: maxNum = i
  if i < minNum: minNum = i

print(minNum, maxNum)