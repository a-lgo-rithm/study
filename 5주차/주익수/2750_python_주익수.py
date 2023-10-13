import heapq
import sys

N = int(sys.stdin.readline().rstrip())

priority_queue = []

for _ in range(N):
    heapq.heappush(priority_queue, int(sys.stdin.readline().rstrip()))

for _ in range(N):
    print(heapq.heappop(priority_queue))
