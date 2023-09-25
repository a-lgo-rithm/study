import sys

A, B = map(int, sys.stdin.readline().split())

reversed_A = int(str(A)[::-1])
reversed_B = int(str(B)[::-1])

print(max(reversed_A, reversed_B))
