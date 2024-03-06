import sys
from collections import deque

n = int(sys.stdin.readline())
fr, to = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
connected = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    connected[x][y] = 1
    connected[y][x] = 1

q = deque([(fr, 0)])
is_connected = False
visited = [0 for _ in range(n+1)]
while q:
    p, d = q.popleft()
    if p == to:
        is_connected = True
        print(d)
        break
    if visited[p] == 0:
        visited[p] = 1
        for i in range(n+1):
            if connected[i][p] == 1 and visited[i] == 0:
                q.append((i, d+1))

if not is_connected:
    print(-1)
    