n = int(input())

# 2가 포함된 개수와 5가 포함된 개수 별개로 저장 (0~500)
count = [[0, 0] for _ in range(501)]
for i in range(1, 501):
    count[i][0] = count[i-1][0]
    count[i][1] = count[i-1][1]
    index = i
    while True:
        if i % 2 != 0 and i % 5 != 0:
            break
        if i % 2 == 0:
            count[index][0] += 1
            i //= 2
        if i % 5 == 0:
            count[index][1] += 1
            i //= 5

print(min(count[n][0], count[n][1]))