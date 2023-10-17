import sys

N, M = map(int, sys.stdin.readline().split())
S = set()
for i in range(N):
    S.add(sys.stdin.readline().rstrip())

count = 0
for i in range(M):
    if sys.stdin.readline().rstrip() in S:
        count += 1

print(count)
