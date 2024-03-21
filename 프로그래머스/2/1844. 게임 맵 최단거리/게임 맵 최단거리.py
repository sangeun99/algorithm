from collections import deque

def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque([(0, 0, 1)]) # 행, 열, 거리
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        i, j, d = q.popleft()
        if i == n-1 and j == m-1:
            answer = d
            break
        if visited[i][j] == 1:
            continue
        visited[i][j] = 1
        for k in range(4):
            n_i = i + move[k][0]
            n_j = j + move[k][1]
            if 0 <= n_i < n and 0 <= n_j < m and maps[n_i][n_j] == 1 and visited[n_i][n_j] == 0:
                q.append((n_i, n_j, d+1))
    return answer