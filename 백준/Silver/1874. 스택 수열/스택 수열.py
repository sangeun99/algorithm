import sys

n = int(sys.stdin.readline()) # [ 1 , ... , n]
result = []
for i in range(n):
    result.append(int(sys.stdin.readline()))

p = []
s = []
i = 1
for r in result:
    while i <= r:
        p.append("+")
        s.append(i)
        i += 1
    
    if s.pop() == r:
        p.append("-")
    else:
        p = []
        break

if p:
    print('\n'.join(p))
else:
    print('NO')