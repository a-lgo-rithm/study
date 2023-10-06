import sys

N = int(sys.stdin.readline())

consults = []
max_profit = 0

for i in range(N):
    T, P = list(map(int, sys.stdin.readline().split()))
    consults.append({'T': T, 'P': P})

def get_max_profit(consults, max_profit, profit, day):
    if day > N:
        return max_profit
    
    if day == N:
        if profit > max_profit:
            max_profit = profit
        return max_profit
    
    if day + consults[day]['T'] <= N:
        max_profit = get_max_profit(consults, max_profit, profit + consults[day]['P'], day + consults[day]['T'])
    
    max_profit = get_max_profit(consults, max_profit, profit, day + 1)
    
    return max_profit

print(get_max_profit(consults, max_profit, 0, 0))