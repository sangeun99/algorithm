import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
arr = sorted(arr)
count = 0

if n == 1:
    if arr[0] == x:
        count = 1
else:
    i = 0
    j = n-1
    while (1):
        n_i = i
        n_j = j
        if arr[i] + arr[j] == x:
            count += 1
            if i < n-1 and arr[i] != arr[i+1]:
                n_j = j-1
            if j > 0 and arr[j] != arr[j-1]:
                n_i = i+1
            if n_j == j and n_i == i:
                n_i = i+1
        elif arr[i] + arr[j] < x:
            n_i = i+1
        else:
            n_j = j-1
        i = n_i
        j = n_j
        if i >= j:
            break
print(count)