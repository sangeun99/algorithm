import sys
import collections

n = int(sys.stdin.readline())
while n > 0:
    log = sys.stdin.readline().strip()
    dl = collections.deque([])
    dr = collections.deque([])
    for l in log:
        if l == "<":
            if len(dl) != 0:
                temp = dl.pop()
                dr.appendleft(temp)
        elif l == ">":
            if len(dr) != 0:
                temp = dr.popleft()
                dl.append(temp)
        elif l == "-":
            if len(dl) != 0:          
                temp = dl.pop()
        else:
            dl.append(l)
    print(''.join(dl)+''.join(dr))
    n -= 1