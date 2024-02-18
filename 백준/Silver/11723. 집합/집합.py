import sys

m = int(sys.stdin.readline())
s = set()
for _ in range(m):
    command = sys.stdin.readline().split()
    if len(command) == 1:
        c = command[0]
    else:
        c, x = command
        x = int(x)
    if c == 'add':
        s.add(x)
    elif c == 'remove':
        if x in s:
            s.remove(x)        
    elif c == 'check':
        if x in s:
            print(1)
        else:
            print(0)
    elif c == 'toggle':
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif c == 'all':
        s = set([i for i in range(21)])
    elif c == 'empty':
        s = set()
