import sys

string = sys.stdin.readline().rstrip()

alphabet = [-1 for _ in range(26)]

for i in string:
    if alphabet[ord(i) - 97] == -1:
        alphabet[ord(i) - 97] = string.index(i)

print(*alphabet)
