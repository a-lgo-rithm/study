import sys

A, B = map(str, sys.stdin.readline().split()) # A, B를 문자열로 받음, 리버스시키기 위함

reversed_A = int(A[::-1]) # 배열을 리버스 시킨 형태를 정수형태로 변환
reversed_B = int(B[::-1])

print(max(reversed_A, reversed_B)) # 둘 중 큰 값을 출력
