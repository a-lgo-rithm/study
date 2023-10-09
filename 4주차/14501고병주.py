n = int(input())

t = []
p = []
dp = [0] * (n+1)

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for j in range(n-1, -1, -1):
    if j + t[j] > n:
        dp[j] = dp[j+1]
    else:
        dp[j] = max(dp[j+t[j]]+p[j], dp[j+1])

print(dp[0])