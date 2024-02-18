import sys
import heapq

n = int(sys.stdin.readline())
q = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(q, x)
    else:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
