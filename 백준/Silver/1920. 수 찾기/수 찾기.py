import sys

def find(element, start, end):
    if start != end:
        mid_index = start + (end - start)//2
        if orig[mid_index] < element:
            return find(element, mid_index+1, end)
        elif orig[mid_index] > element:
            return find(element, start, mid_index)
        else:
            return 1
    else:
        return 0
    

n = int(sys.stdin.readline())
orig = list(map(int, sys.stdin.readline().split()))
orig.sort()
m = int(sys.stdin.readline())
comp = list(map(int, sys.stdin.readline().split()))

for c in comp:
    print(find(c, 0, n))