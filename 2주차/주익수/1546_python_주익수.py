import sys

N = int(sys.stdin.readline())
score_list = list(map(int, sys.stdin.readline().split()))
score_list.sort()

max_value = score_list[-1]

for i in range(N):
    score_list[i] = score_list[i] / max_value * 100

average = sum(score_list) / N

print(round(average, 6))
