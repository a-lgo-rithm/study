import heapq
import sys

N, k = map(int, sys.stdin.buffer.readline().split())
peoples = list(map(int, sys.stdin.readline().split()))

heapq.heapify(peoples)
for i in range(N - k):
    heapq.heappop(peoples)  # k번째로 작은 값이 맨 앞에 오게 됨

print(heapq.heappop(peoples))  # k번째로 작은 값 출력
