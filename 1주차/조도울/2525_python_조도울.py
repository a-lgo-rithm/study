hour, minute = map(int, input().split(" "))
time = int(input())

print((hour + ((minute + time) // 60)) % 24, (minute + time) % 60)