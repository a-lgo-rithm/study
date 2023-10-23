import sys

N = int(sys.stdin.readline().rstrip())

strings = []
prefix_dict = dict()
for index in range(N):
    strings.append(sys.stdin.readline().rstrip())

# 입력받은 모든 문자열들의 접두사들을 dict 형태로 저장해줍니다.
# 최대 20000 * 100 가지의 경우의 수의 접두사들이 발생하므로 리스트가 아닌 dictionary 형태로 정의했습니다.
for index in range(N):
    for prefix_length in range(1, len(strings[index]) + 1):  # 각 문자열들이 가질 수 있는 모든 접두사 경우의 수를 추가합니다.
        if strings[index][:prefix_length] in prefix_dict.keys():  # 이미 다른 문자열에서 존재하는 접두사일 경우, 리스트에 추가해줍니다.
            prefix_dict[strings[index][:prefix_length]].append(index)
        else:  # 최초 접두사일 경우, 리스트로 정의합니다.
            prefix_dict[strings[index][:prefix_length]] = [index]

for i in prefix_dict.keys():  # 각 접두사 별 인덱스 배열을 정렬해줍니다. (O(20_000 * 100) * O
    prefix_dict[i].sort()

max_prefix = -1  # 최대 접두사를 비교하기 위한 변수입니다.
answer_list = [0, 1]  # 정답 배열입니다. 최장 접두사가 0인 경우, 0, 1을 출력해야 하므로 해당 값으로 초기화하였습니다.
for index in range(N):  # 각 문자열을 돌면서 : O(20_000)
    for prefix_length in range(1, len(strings[index]) + 1):  # 접두사들을 만들어서 비교를 진행합니다. O(100)
        if prefix_dict[strings[index][:prefix_length]] is not None:  # 접두사 집합에 지금 접두사가 존재하는 경우
            for prefix_index in prefix_dict[
                strings[index][:prefix_length]]:  # 해당 접두사 집합의 문자열 인덱스 리스트를 순회하면서 (O(20_000))
                if prefix_index != index and max_prefix < prefix_length:  # 해당 인덱스가 지금 비교중인 인덱스가 아니면서 최장 접두사인 경우
                    max_prefix = prefix_length  # 최장 접두사 길이에 해당 값을 넣어주고
                    answer_list = [index, prefix_index]  # 정답 배열을 초기화합니다.

answer_list.sort()  # 입력된 순서대로 출력해야 하니 정렬을 진행합니다.
print(strings[answer_list[0]], strings[answer_list[1]], sep='\n')
