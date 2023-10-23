import sys

M, N = map(int, sys.stdin.readline().split())


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(M, N + 1):
    if i == 1:
        continue
    if is_prime(i):
        print(i)
