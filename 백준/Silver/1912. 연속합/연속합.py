import sys

n = int(input())
dp = list(map(int, sys.stdin.readline().split()))
# dp[i]는 i가 포함된 연속 수 중 최대를 구함

for i in range(1, n):
  dp[i] = max(dp[i], dp[i-1]+dp[i])

print(max(dp))