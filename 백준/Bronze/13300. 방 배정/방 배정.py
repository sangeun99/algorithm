import sys
import math

n, k = map(int, sys.stdin.readline().split())
stud = [[0, 0] for _ in range(6)] # 남, 여

for i in range(n): # 최대 1000회
    s, y = map(int, sys.stdin.readline().split())
    stud[y-1][s] += 1

rooms = 0
for i in range(6):
    for j in range(2):
        rooms += math.ceil(stud[i][j]/k)
print(rooms)