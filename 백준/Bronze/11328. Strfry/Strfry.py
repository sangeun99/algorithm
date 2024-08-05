import sys

n = int(sys.stdin.readline())
for _ in range(n):
    w1, w2 = sys.stdin.readline().split()
    if len(w1) != len(w2):
        print("Impossible")
    else:
        l = len(w1) # 최대 길이: 1000
        # 문자열 구성된 알파벳 개수가 일치하면 Possible
        w1_c = [0 for _ in range(26)]
        w2_c = [0 for _ in range(26)]
        for i in range(l):
            w1_c[ord(w1[i])-97] += 1
            w2_c[ord(w2[i])-97] += 1
        if w1_c == w2_c:
            print("Possible")
        else:
            print("Impossible")