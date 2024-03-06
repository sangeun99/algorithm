import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
connected = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    t1, t2 = map(int, sys.stdin.readline().split())
    connected[t1][t2] = 1
    connected[t2][t1] = 1

visited = [0 for _ in range(n+1)]
count = -1
q = [1]
while q:
    i = q.pop()
    if visited[i] == 0:
        visited[i] = 1
        count += 1
        for j in range(1, n+1):
            if connected[i][j] == 1 and visited[j] == 0:
                q.append(j)
print(count)
