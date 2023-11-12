n = int(input())

# 바텀업 방식을 이용
m = [0 for i in range(1001)]
m[1] = 1
m[2] = 2

for i in range(3, 1001) :
  m[i] = m[i-1] + m[i-2]

print(m[n] % 10007)