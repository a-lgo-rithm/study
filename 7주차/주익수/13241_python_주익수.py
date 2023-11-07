import sys

A, B = map(int, sys.stdin.readline().split())


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


g = gcd(max(A, B), min(A, B))
print(A * B // g)