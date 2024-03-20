import sys

n, m = map(int, sys.stdin.readline().split())
table = [[i for i in list(map(int, sys.stdin.readline().split()))] for _ in range(n)]

# 구간합 배열 만들기 ((0, 0) 부터 (y, x) 까지의 합)
s_t = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            s_t[i][j] = table[i][j]
        elif i == 0:
            s_t[i][j] = s_t[i][j-1] + table[i][j]
        elif j == 0:
            s_t[i][j] = s_t[i-1][j] + table[i][j]
        else:
            s_t[i][j] = s_t[i-1][j] + s_t[i][j-1] - s_t[i-1][j-1] + table[i][j]

for _ in range(m):
    # x행 y열
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    if x1 == 1 and y1 == 1:
        part_sum = s_t[x2-1][y2-1]
    elif x1 == 1:
        part_sum = s_t[x2-1][y2-1] - s_t[x2-1][y1-2]
    elif y1 == 1:
        part_sum = s_t[x2-1][y2-1] - s_t[x1-2][y2-1]
    else:
        part_sum = s_t[x2-1][y2-1] - s_t[x1-2][y2-1] - s_t[x2-1][y1-2] + s_t[x1-2][y1-2]
    print(part_sum)