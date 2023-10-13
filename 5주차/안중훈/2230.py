import sys

N, M = list(map(int, sys.stdin.readline().split()))

A = []
minimumDifference = 2000000000
pointer1 = 0
pointer2 = 0

for i in range(N):
  A.append(int(sys.stdin.readline()))

A.sort()

while pointer1 < N and pointer2 < N:
  difference = abs(A[pointer2] - A[pointer1])

  if difference >= M:
    if difference < minimumDifference:
      minimumDifference = difference
    pointer1 += 1
  else:
    pointer2 += 1

print(minimumDifference)
