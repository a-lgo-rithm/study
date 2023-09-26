import sys

S = str(sys.stdin.readline())

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    print(S.find(i), end=' ')
    