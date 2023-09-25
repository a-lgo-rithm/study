import sys

tree = dict()
for line in sys.stdin: # 입력이 끝날 때까지 계속 입력받음
    if line.rstrip() in tree: # 입력받은 값이 이미 딕셔너리에 있으면 1을 더함
        tree[line.rstrip()] += 1
    else: # 입력받은 값이 딕셔너리에 없으면 새로운 나무이므로 1을 넣음
        tree[line.rstrip()] = 1

total = sum(tree.values()) # 총 나무의 개수를 구함

for key in sorted(tree.keys()): # 사전순으로 출력하라했으니, 키를 정렬해서 순회
    print(key, '%.4f' % (tree[key] / total * 100)) # 소수점 4자리까지 출력하라고 했으니, 소수점 4자리까지 출력
