import sys

N = int(sys.stdin.readline())

for i in range(N):
    if i + sum(map(int, str(i))) == N:
        print(i)
        break
    
    if i == N - 1:
        print(0)
    