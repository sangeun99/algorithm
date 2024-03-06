import sys
from collections import deque

def bfs(n, k):
    if n == k:
        return 0
    q = deque([(n, 0)])
    visited = [0 for _ in range(100000+1)]
    while q:
        p, d = q.popleft()
        if visited[p] == 0:
            visited[p] = 1
            if 0 <= p*2 <= 100000:
                if p*2 == k:
                    return d+1
                q.append([p*2, d+1])
            if 0 <= p+1 <= 100000:
                if p+1 == k:
                    return d+1
                q.append([p+1, d+1])
            if 0 <= p-1 <= 100000:
                if p-1 == k:
                    return d+1
                q.append([p-1, d+1])

n, k = map(int, sys.stdin.readline().split())
print(bfs(n, k))