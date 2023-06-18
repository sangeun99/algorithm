import sys

def partOfStr(part, str) :
    counter = 0
    for i in str :
        if counter == len(part) :
            return True
        elif part[counter] == i :
            counter += 1
    return False

while 1 :
    s, t = sys.stdin.readline().split()
    if (partOfStr(s,t)) :
        print('Yes')
    else :
        print('No')