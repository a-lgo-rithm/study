import sys
inputs = sys.stdin.readline 

M, N = map(int,inputs().split())

primeList = [2]
for i in range(1,N+1):
  if i == 1: continue
  if i == 2: 
    primeList.append(i)
    if i >= M:
      print(i)
  for prime in primeList:
    if i % prime == 0:
      break
    if prime == primeList[-1] or i**0.5 < prime:
      primeList.append(i)
      if i >= M:
        print(i)
      break