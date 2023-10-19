import sys
inputs = sys.stdin.readline 

N = int(inputs())
wordList = []
maxEqaulLength = 0
for _ in range(N):
  wordList.append(inputs().rstrip())
S, T = '', ''
sortedWordList = sorted(wordList)
maxEqaulWordSet = set()

for i in range(1, N):
  prevWord = sortedWordList[i-1]
  currentWord = sortedWordList[i]
  shortLen = min(len(prevWord), len(currentWord))

  eqaulCount = 0
  for j in range(shortLen):
    if prevWord[j] != currentWord[j]:
      break
    eqaulCount += 1
  if maxEqaulLength < eqaulCount:
    maxEqaulLength = eqaulCount
    maxEqaulWordSet.clear()
    maxEqaulWordSet.update([prevWord, currentWord])
  elif maxEqaulLength == eqaulCount:
    maxEqaulWordSet.update([prevWord, currentWord])

for word in wordList:
  if word in maxEqaulWordSet:
    if S == '': 
      S = word
    elif S[:maxEqaulLength] == word[:maxEqaulLength]:
      T = word
      break

print(S)
print(T)