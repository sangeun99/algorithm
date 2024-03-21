from collections import deque

def solution(maps):
    answer = []
    is_none = True
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = deque([])
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                is_none = False
                q.append((i, j))
                days = 0
                while q:
                    x, y = q.popleft()
                    if visited[x][y] == 1:
                        continue
                    visited[x][y] = 1
                    days += int(maps[x][y])
                    for k in range(4):
                        n_x = x + d[k][0]
                        n_y = y + d[k][1]
                        if 0 <= n_x < len(maps) and 0 <= n_y < len(maps[0]) and maps[n_x][n_y] != 'X' and visited[n_x][n_y] == 0:
                            q.append((n_x, n_y))
                answer.append(days)
    if is_none:
        answer = [-1]
    answer.sort()
    return answer