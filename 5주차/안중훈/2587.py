import sys

arrLen = 5

arr = []

for i in range(arrLen):
    arr.append(int(sys.stdin.readline()))

arr.sort()

average = sum(arr) / arrLen
middle = arr[arrLen // 2]

print(int(average))
print(middle)