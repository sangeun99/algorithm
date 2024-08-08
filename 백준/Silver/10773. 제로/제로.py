import sys

k = int(sys.stdin.readline())
l = []
while k:
    n = int(sys.stdin.readline())
    if n == 0:
        l.pop()
    else:
        l.append(n)
    k -= 1
print(sum(l))