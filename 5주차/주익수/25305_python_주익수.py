import heapq
import sys

N, k = map(int, sys.stdin.buffer.readline().split())
peoples = list(map(int, sys.stdin.readline().split()))

heapq.heapify(peoples)
for i in range(N - k):
    heapq.heappop(peoples)

print(heapq.heappop(peoples))
