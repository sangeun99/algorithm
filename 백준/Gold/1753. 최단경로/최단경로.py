import sys
import math
import heapq

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline()) - 1
adj = [[] for _ in range(v)]
for i in range(e):
    st, en, we = map(int, sys.stdin.readline().split())
    adj[st-1].append((en-1, we))

# 시작 노드로부터의 거리
dist = [math.inf for _ in range(v)]
dist[k] = 0
hq = []
heapq.heappush(hq, (0, k)) # distance, index

while hq:
    min_w, min_s = heapq.heappop(hq)
    for en, we in adj[min_s]:
        if dist[min_s] + we < dist[en]:
            dist[en] = dist[min_s] + we
            heapq.heappush(hq, (dist[en], en))

for d in dist:
    if d == math.inf:
        print("INF")
    else:
        print(d)