import sys
inputs = sys.stdin.readline

N = int(inputs())

sortedList = []
for _ in range(N):
  sortedList.append(int(inputs())) 

sortedList.sort()

for i in sortedList:
  print(i) 
