import sys

string = sys.stdin.readline().rstrip()

alphabet = [-1 for _ in range(26)] # 알파벳 배열을 -1로 초기화

for i in string:
    if alphabet[ord(i) - 97] == -1: # 소문자만 입력되므로, 아스키 코드를 이용하여 알파벳 배열에 인덱스를 저장한다. 또한 -1이면 처음 등장한 것
        alphabet[ord(i) - 97] = string.index(i) # 처음 등장한 인덱스를 저장한다.

print(*alphabet) # 참조를 위해 *를 붙여 출력한다. 이 경우 굳이 for문을 돌릴 필요가 없다.
