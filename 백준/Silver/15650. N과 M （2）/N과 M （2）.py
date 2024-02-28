import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
for combi in combinations(range(1, n+1), m):
    for i in combi:
        print(i, end=' ')
    print()