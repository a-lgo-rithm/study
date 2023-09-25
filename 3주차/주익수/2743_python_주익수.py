import sys

string = sys.stdin.readline().rstrip()

length = 0 # 길이 값 초기화

for i in string: # 문자열을 순회하면서 길이를 증가시킴
    length += 1

print(length) # 길이 출력
