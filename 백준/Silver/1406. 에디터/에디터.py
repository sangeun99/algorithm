import sys
import collections

org = sys.stdin.readline().strip()
m = int(sys.stdin.readline())
dl = collections.deque(list(org))
dr = collections.deque([])
while m:
    comm = list(sys.stdin.readline().split())
    if comm[0] == "L":
        if dl:
            temp = dl.pop()
            dr.appendleft(temp)
    elif comm[0] == "D":
        if dr:
            temp = dr.popleft()
            dl.append(temp)
    elif comm[0] == "B":
        if dl:
            dl.pop()
    elif comm[0] == "P":
        dl.append(comm[1])
    m -= 1
print(''.join(dl)+''.join(dr))