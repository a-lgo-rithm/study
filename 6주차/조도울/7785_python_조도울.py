import sys
inputs = sys.stdin.readline 

N = int(inputs())
logSet = set()

for _ in range(N):
  user, log = inputs().split()
  if log == "enter":
    logSet.add(user)
  else:
    logSet.remove(user)
sortedLogList = list(logSet)
sortedLogList.sort(reverse=True)
print(*sortedLogList, sep='\n')