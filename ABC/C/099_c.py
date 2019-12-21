import math
n = int(input())
dp = [float("inf")] * (10 ** 5 + 10)
dp[0] = 0
for i in range(1,n + 1):
  power = 1
  while n >= power:
    dp[i] = min(dp[i],dp[i - power] + 1)
    power *= 6
  power = 1
  while n >= power:
    dp[i] = min(dp[i],dp[i - power] + 1)
    power *= 9
print(dp[n])