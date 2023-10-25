import sys

inputs = sys.stdin.readline 

T = int(inputs())
leastCommonMultipleList = []

for _ in range(T):
  A, B = map(int,inputs().split())
  maxNumber = max(A, B)
  minNumber = min(A, B)

  while True:
    remainder = maxNumber % minNumber
    if remainder == 0:
      break
    maxNumber, minNumber = minNumber, remainder
  leastCommonMultipleList.append((A * B) // minNumber)

print(*leastCommonMultipleList, sep='\n')