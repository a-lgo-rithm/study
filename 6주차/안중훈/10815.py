import sys

N = int(sys.stdin.readline())
sangGeunCards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

sangGeunCards.sort()

def binarySearch(target, start, end):
  if start > end:
    return 0

  middle = (start + end) // 2

  if sangGeunCards[middle] == target:
    return 1
  elif sangGeunCards[middle] > target:
    return binarySearch(target, start, middle - 1)
  else:
    return binarySearch(target, middle + 1, end)
    
for card in cards:
  print(binarySearch(card, 0, N - 1), end=' ')