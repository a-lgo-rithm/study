import sys

N = int(sys.stdin.readline())

employees = {}

for i in range(N):
  name, status = sys.stdin.readline().split()

  if status == 'enter':
    employees[name] = True
  else:
    del employees[name]

employees = sorted(employees.keys(), reverse=True)

for employee in employees:
  print(employee)