import sys
inputs = sys.stdin.readline

N, k = map(int, inputs().split())
sortedList = sorted(list(map(int, inputs().split())))

print(sortedList[-k])
