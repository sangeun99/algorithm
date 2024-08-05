import sys

n, k = map(int, sys.stdin.readline().split())
n_l = [i+1 for i in range(n)]

ind = -1
print('<', end='')
while n_l:
    ind += k
    ind %= len(n_l)
    if len(n_l) > 1:
        print(n_l[ind], end=', ')
    else:
        print(n_l[ind], end='')
    n_l.remove(n_l[ind])
    ind -= 1
print('>', end='')