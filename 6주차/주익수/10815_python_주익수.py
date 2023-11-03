import sys

N = int(sys.stdin.readline().rstrip())
N_nums = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().rstrip())
M_nums = list(map(int, sys.stdin.readline().split()))

for i in M_nums:
    if i in N_nums:
        print(1, end=' ')
    else:
        print(0, end=' ')
