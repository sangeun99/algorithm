n = int(input())

i = 1 # 분모, 분자의 합은 i+1가 됨
while (True):
  if (n > i):
    n -= i
    i += 1
  else:
    break

# p / q
# i + 1이 짝수면 q가 1부터 ... -> q = n, p = i + 1 - q
# i + 1이 홀수면 p가 1부터 ... -> p = n, q = i + 1 - p

if (i % 2 == 1):
  q = n
  p = i + 1 - q
else:
  p = n
  q = i + 1 - p

answer = str(p) + "/" + str(q)
print(answer)