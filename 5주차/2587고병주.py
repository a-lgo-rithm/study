
arr = []
result = 0

for _ in range(5):
    x = int(input())
    arr.append(x)
    result += x

print(int(result/5))
print(arr[2])
