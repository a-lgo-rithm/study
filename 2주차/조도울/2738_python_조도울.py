import sys

N, M = map(int,sys.stdin.readline().split())

A, B = [], []
sumList = []

for _ in range(0, N):
  A.append(list(map(int,sys.stdin.readline().split())))

for _ in range(0, N):
  B.append(list(map(int,sys.stdin.readline().split())))

for i in range(0, N):  
  sumList.append([x+y for x,y in zip(A[i], B[i])])
  print(' '.join(map(str, sumList[i])))