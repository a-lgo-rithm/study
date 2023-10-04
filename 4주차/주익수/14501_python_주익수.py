import sys

N = int(sys.stdin.readline().strip())
schedule = []

for i in range(N):
    T, P = map(int, sys.stdin.readline().split())
    schedule.append((T, P))

dp = [0 for _ in range(N + 1)]

for i in range(N):
    for j in range(i + schedule[i][0], N + 1):
        if dp[j] < dp[i] + schedule[i][1]:  # 이중 for문을 돌면서 dp[j]에 최대값을 저장한다.
            dp[j] = dp[i] + schedule[i][1]  # dp[j]에는 j일까지의 최대값이 저장된다.
    print(dp)

print(dp[-1])
