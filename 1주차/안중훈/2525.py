timestamp = input().split(' ')
timeToCook = int(input())

hour = int(timestamp[0])
minute = int(timestamp[1])

minute += timeToCook

completeHour = hour + (minute // 60)
completeMinute = minute % 60

if completeHour >= 24:
    completeHour = completeHour % 24

print(completeHour, completeMinute)