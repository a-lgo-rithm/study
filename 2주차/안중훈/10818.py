import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

print(min(X), max(X))