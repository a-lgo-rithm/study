import sys

inputs = sys.stdin.readline 

A, B = map(int,inputs().split())
maxNumber = max(A, B)
minNumber = min(A, B)

while True:
  remainder = maxNumber % minNumber
  if remainder == 0:
    break
  maxNumber, minNumber = minNumber, remainder
  
print((A * B) // minNumber)