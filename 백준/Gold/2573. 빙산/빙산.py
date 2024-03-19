import sys
import copy
from collections import deque

n, m = map(int, sys.stdin.readline().split())
ice = [[i for i in list(map(int, sys.stdin.readline().split()))] for _ in range(n)]

def bfs(q):
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        i, j = q.popleft()
        m_c = 0
        for k in range(4):
            n_x = i + d[k][0]
            n_y = j + d[k][1]
            if ice[n_x][n_y] == 0:
                m_c += 1
            if 0 <= n_x < n and 0 <= n_y < m and ice[n_x][n_y] > 0 and visited[n_x][n_y] == 0:
                visited[n_x][n_y] = 1
                q.append((n_x, n_y))
        next_ice[i][j] = max(ice[i][j]-m_c, 0)

year = 0
next_ice = copy.deepcopy(ice)
q = deque([])
while True:
    is_done = True
    visited = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if ice[i][j] > 0 and visited[i][j] == 0:
                is_done = False
                visited[i][j] = 1
                q.append((i, j))
                bfs(q)
                count += 1
    ice = copy.deepcopy(next_ice)
    if is_done:
        print(0)
        break
    if count >= 2:
        print(year)
        break
    year += 1