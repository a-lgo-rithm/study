import sys

N, M = map(int,sys.stdin.readline().split())

basket = list(range(1,N + 1))

for _ in range(0, M):
  i, j = map(int,sys.stdin.readline().split())
  basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

print(' '.join(map(str, basket)))