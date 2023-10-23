import sys
inputs = sys.stdin.readline 

N, M = map(int, inputs().split())
wordSet = set()
wordCount = 0

for _ in range(N):
  wordSet.add(inputs().rstrip())

for _ in range(M):
  checkString = inputs().rstrip()
  if checkString in wordSet:
    wordCount += 1
print(wordCount)