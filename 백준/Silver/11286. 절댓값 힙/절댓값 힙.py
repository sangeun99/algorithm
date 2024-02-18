import sys
import heapq

n = int(sys.stdin.readline())
q = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)
    else:
        heapq.heappush(q, (abs(x), x))