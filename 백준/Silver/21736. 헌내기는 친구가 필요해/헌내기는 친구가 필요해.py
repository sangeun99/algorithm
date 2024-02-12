import sys

n, m = map(int, sys.stdin.readline().split())
campus = []
for _ in range(n):
    campus.append(list(sys.stdin.readline().strip()))
visited = [[0 for _ in range(m)] for _ in range(n)]

count = 0
d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            s = [(i, j)]
            break

while s:
    x, y = s.pop()
    if visited[x][y] == 1:
        continue
    visited[x][y] = 1
    if campus[x][y] == 'P':
        count += 1
    for d_i in range(4):
        d_x, d_y = d[d_i]
        if 0 <= x+d_x < n and 0 <= y+d_y < m and visited[x+d_x][y+d_y] == 0 and campus[x+d_x][y+d_y] != 'X':
            s.append((x+d_x, y+d_y))

if count:
    print(count)
else:
    print('TT')