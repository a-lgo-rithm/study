import itertools
import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

nCr = list(itertools.combinations(arr, 3))  # arr 배열에 입력받은 중, 조합 수행, nC3 형태

answer = 0  # 초기 선언값
min_value = sys.maxsize  # 초기 차이값

for i in nCr:  # 생성된 조합(튜플) 리스트를 순회
    sum_combination = sum(i)  # 튜플의 총합 값
    diff = M - sum_combination  # M 값과 비교 수행, abs()를 사용하지 않은 것은 넘으면 안되기 때문

    if 0 <= diff < min_value:  # 음수의 경우, M 값보다 더 큰 값이므로 제외
        min_value = diff
        answer = sum_combination

print(answer)
