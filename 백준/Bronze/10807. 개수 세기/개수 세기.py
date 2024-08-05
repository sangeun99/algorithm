import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split())) # 최대 100개, -100과 100 사이 정수 모음
v = int(sys.stdin.readline())

cnt = 0
for i in range(n):
    if l[i] == v:
        cnt += 1

print(cnt)