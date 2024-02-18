import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)][::-1]

count = 0
for c in coins:
    if (k // c > 0):
        count += k // c
        k = k % c
print(count)