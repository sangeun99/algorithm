from collections import deque

def isChangable(b, t):
    n = len(b)
    diff = 0
    for i in range(n):
        if b[i] != t[i]:
            if diff != 0:
                return False
            diff += 1
    return True

def solution(begin, target, words):
    q = deque([(begin, 0)])
    if target not in words:
        return 0
    while q:
        w, c = q.popleft()
        if w == target:
            return c
        for i in range(len(words)):
            if isChangable(w, words[i]):
                q.append((words[i], c+1))        
    return 0