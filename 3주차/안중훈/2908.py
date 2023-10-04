import sys

A, B = list(map(str, sys.stdin.readline().split()))

a = A[::-1]
b = B[::-1]

if int(a) > int(b):
    print(a)
else:
    print(b)