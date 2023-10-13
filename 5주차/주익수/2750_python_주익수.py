import heapq
import sys

N = int(sys.stdin.readline().rstrip())

priority_queue = []

for _ in range(N):
    heapq.heappush(priority_queue, int(sys.stdin.readline().rstrip())) # heapq는 최소 힙이므로, 최소 힙으로 만들어줌

for _ in range(N):
    print(heapq.heappop(priority_queue)) # 최소 힙이므로, 최소값부터 출력
