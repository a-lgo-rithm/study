import sys

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

A = []

for _ in range(N):
    A.append(int(sys.stdin.readline().rstrip()))

A.sort()
i, j = 0, 0
min_gap = sys.maxsize
while i < N and j < N:
    gap = A[j] - A[i]
    if gap >= M:
        min_gap = min(gap, min_gap)
        i += 1

    else:
        j += 1

print(min_gap)
