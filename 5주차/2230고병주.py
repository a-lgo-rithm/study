n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()
left, right = 0, 0
result = int(2000000000)

while left < n and right < n:
    if arr[right] - arr[left] < m:
        right += 1
    else:
        result = min(result, arr[right] - arr[left])
        left += 1

print(result)