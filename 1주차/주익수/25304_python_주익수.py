import sys

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
item_arr = [] # [가격, 개수] 형태로 입력 받기 위한 아이템 리스트 선언
price_sum = 0  # 총 가격 비교를 위한 변수

for i in range(N): # 아이템 리스트에 입력 받기
    item_arr.append(list(map(int, sys.stdin.readline().split())))

for itme_price, item_count in item_arr: # 아이템 리스트를 순회하며 총 가격 계산
    price_sum += itme_price * item_count # 가격 * 개수를 총 가격 변수에 더해줌

if price_sum == X: # 총 가격이 입력 받은 가격과 같으면 Yes 출력
    print("Yes")
else: # 총 가격이 입력 받은 가격과 다르면 No 출력
    print("No")
