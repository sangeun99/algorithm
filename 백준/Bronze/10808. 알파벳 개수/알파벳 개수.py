import sys

s = sys.stdin.readline()
alphabet =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
count = [0 for _ in range(26)]

for i in range(len(s)):
    for j in range(26):
        if s[i] == alphabet[j]:
            count[j] += 1

for i in range(26):
    print(count[i], end=' ')