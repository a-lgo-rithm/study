import heapq
import sys

N = int(sys.stdin.readline())

heap = list(map(int, sys.stdin.readline().split()))  # 정렬을 수행할 리스트를 입력 받습니다.
heapq.heapify(heap)  # 리스트를 힙으로 변환합니다. 이로 인해 pop을 진행할 경우, 최솟값부터 pop을 진행합니다.

sorted_list = []

for i in range(len(heap)):
    sorted_list.append(heapq.heappop(heap))  # 최솟값부터 정렬된 리스트에 추가합니다.

print(sorted_list[0], sorted_list[-1])  # 최솟값과 최댓값을 출력합니다.
