import sys
inputs = sys.stdin.readline

N, M = map(int, inputs().split())

A = []
L, R = 0, 0
gap = -1
for _ in range(N):
  A.append(int(inputs()))

A.sort()

while L < N - 1 and R < N:
  newGap = A[R] - A[L]
  if newGap > M:
    gap = newGap if newGap < gap or gap == -1 else gap
    L += 1
  elif newGap == M:
    gap = newGap
    break
  else:
    R += 1
print(gap)