from collections import deque

def solution(n, computers):
    def bfs(q):
        while q:
            i = q.popleft()
            if visited[i] == 0:
                visited[i] = 1
                for c in range(n):
                    if computers[i][c] == 1 and visited[c] == 0:
                        q.append(c)
                
    answer = 0
    visited = [0 for _ in range(n)]
    q = deque([])
    for i in range(n):
        if not visited[i]:
            q.append(i)
            bfs(q)
            answer += 1
    return answer