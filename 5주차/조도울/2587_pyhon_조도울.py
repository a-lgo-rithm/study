import sys
inputs = sys.stdin.readline

sortedList = []
for _ in range(5):
  sortedList.append(int(inputs())) 

sortedList.sort()
print(int(sum(sortedList) / 5)) 
print(sortedList[2])
