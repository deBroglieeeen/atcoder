n = int(input())
field = list(map(int,input().split()))
dp = [float("inf")]*n

dp[0] = 0

for i in range(1,n):
  dp[i] = min(dp[i],dp[i - 1] + abs(field[i] - field[i - 1]))
  if i > 1:
    dp[i] = min(dp[i],dp[i - 2] + abs(field[i] - field[i - 2]))
print(str(dp.pop()))