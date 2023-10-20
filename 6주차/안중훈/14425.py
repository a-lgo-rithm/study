import sys

N, M = list(map(int, sys.stdin.readline().split()))

S = {}
strings = []
answer = 0

for i in range(N):
  S[sys.stdin.readline()] = True

for i in range(M):
  strings.append(sys.stdin.readline())

for string in strings:
  if string in S:
    answer += 1

print(answer)