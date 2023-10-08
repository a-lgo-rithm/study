import sys
inputs = sys.stdin.readline

def adviceListSchdule(day):
  sum = 0

  while day < N:
    caseSum = 0
    newDay = day + adviceList[day]["time"]
    
    if newDay > N:
      caseSum += 0
    elif newDay == N:
      caseSum += adviceList[day]["price"]
    else:
      caseSum += adviceListSchdule(newDay) + adviceList[day]["price"]
    
    if sum < caseSum: sum = caseSum
    day += 1
  return sum
    
N = int(inputs())

adviceList = []

for _ in range(N):
  T, P = map(int, inputs().split())
  adviceList.append({"time": T, "price": P}) 

print(adviceListSchdule(0))