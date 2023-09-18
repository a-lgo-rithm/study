import sys

A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())

B += C # 분 더하기
A += B // 60 # 초과하는 시간만큼 더 해주기
B %= 60 # 초과하는 분은 버리기
A %= 24 # 초과하는 시간은 버리기

print(A, B)