import sys
import heapq

num_array = []
for _ in range(5):
    heapq.heappush(num_array, int(sys.stdin.readline().rstrip()))


print(sum(num_array) // 5)
heapq.heappop(num_array)
heapq.heappop(num_array)
print(heapq.heappop(num_array))
