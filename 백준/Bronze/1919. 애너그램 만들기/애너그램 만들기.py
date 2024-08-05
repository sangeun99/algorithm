import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

a_c = [0 for _ in range(26)]
for i in range(len(a)):
    a_c[ord(a[i])-97] += 1
b_c = [0 for _ in range(26)]
for i in range(len(b)):
    b_c[ord(b[i])-97] += 1

cnt = 0
for i in range(26):
    cnt += abs(a_c[i]-b_c[i])
print(cnt)