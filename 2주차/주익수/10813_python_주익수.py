import sys

N, M = map(int, sys.stdin.readline().split())

ball_list = [i for i in range(1, N + 1)]
for i in range(M):
    i, j = map(int, sys.stdin.readline().split())
    ball_list[i - 1], ball_list[j - 1] = ball_list[j - 1], ball_list[i - 1]

print(*ball_list)
