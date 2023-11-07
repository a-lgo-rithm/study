import sys


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    print(A * B // gcd(A, B))

#     num = max(A, B)
#
#     while True:
#         if num % A == 0 and num % B == 0:
#             print(num)
#             break
#         num += 1
# 시간초과
