import sys
inputs = sys.stdin.readline 

treeDict = {}
allCount = 0
while True:
  tree = inputs().rstrip()

  if not tree:
    break
  elif tree in treeDict:
    treeDict[tree] += 1
  else:
    treeDict[tree] = 1 
  allCount += 1

sortedList = sorted(list(treeDict.keys()))

for i in sortedList:
  print('{} {:.4f}'.format(i, (treeDict[i] / allCount) * 100))