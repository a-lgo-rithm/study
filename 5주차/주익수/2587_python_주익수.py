import sys
import heapq

num_array = []
for _ in range(5):
    heapq.heappush(num_array, int(sys.stdin.readline().rstrip()))


print(sum(num_array) // 5)
heapq.heappop(num_array) # 첫 번째 값 제거
heapq.heappop(num_array) # 두 번째 값 제거
print(heapq.heappop(num_array)) # 세 번째 값 출력
