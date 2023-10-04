import sys


def get_digit_sum(num: int):  # 각 자릿수 별 합을 계산해주는 함수
    digit_sum = 0

    for i in str(num):  # 숫자를 문자열 형태로 변경하여 순회 진행
        digit_sum += int(i)  # 각 자릿수 별 타입 변경 후 총합 진행

    return digit_sum  # 결과 반환


N = int(sys.stdin.readline())

answer = 0
for i in range(1, N + 1):  # N보다 큰 경우에서 분해합이 존재하지 않으므로 N + 1까지
    decomposed_sum = get_digit_sum(i) + i  # 분해합 계산
    if decomposed_sum == N:  # N의 분해합일 경우, 해당 값으로 초기화
        answer = i
        break

print(answer)
