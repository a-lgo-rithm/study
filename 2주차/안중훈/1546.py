import sys

N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
M = max(scores)

phoenixScores = list(map(lambda x: x / M * 100, scores))
print(sum(phoenixScores) / N)