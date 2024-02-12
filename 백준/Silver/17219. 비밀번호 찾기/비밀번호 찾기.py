import sys

n, m = map(int, sys.stdin.readline().split())
p_dict = dict()
for _ in range(n):
    site, pw = sys.stdin.readline().split()
    p_dict[site] = pw
for _ in range(m):
    site = sys.stdin.readline().strip()
    print(p_dict[site])