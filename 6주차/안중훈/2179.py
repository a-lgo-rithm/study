import sys

N = int(sys.stdin.readline())

strings = []
maxPrefixLength = 0

for i in range(N):
  strings.append(sys.stdin.readline())

answers = []

sortedStrings = sorted(strings)

for i in range(N - 1):
  first = sortedStrings[i]
  second = sortedStrings[i + 1]

  length = 0

  for j in range(len(first)):
    if first[j] == second[j]:
      length += 1
    else:
      break

  if length > maxPrefixLength:
    maxPrefixLength = length
    answers = [[first, second]]
  elif length == maxPrefixLength:
    answers.append([first, second])

realAnswer = []
index1 = 19999

for answer in answers:
  foundIndex1 = strings.index(answer[0])
  foundIndex2 = strings.index(answer[1])

  if foundIndex1 < index1:
    index1 = foundIndex1
    realAnswer = [answer[0], answer[1]]
    
  if foundIndex2 < index1:
    index1 = foundIndex2
    realAnswer = [answer[1], answer[0]]

print(realAnswer[0], realAnswer[1], sep='')