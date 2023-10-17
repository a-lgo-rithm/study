import sys

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

A = []

for _ in range(N):
    A.append(int(sys.stdin.readline().rstrip()))

A.sort()
i, j = 0, 0  # 차이를 구해야 하므로 0, 0에서 시작
min_gap = sys.maxsize  # python 최대 사이즈 값

while i < N and j < N: # M이 0인 경우, i에 대한 경우도 생각해주어야 함
    gap = A[j] - A[i]
    if gap >= M:
        min_gap = min(gap, min_gap)
        i += 1

    else:
        j += 1

print(min_gap)
