mod = 1000000007
n,m = map(int,input().split())
A = [int(input()) for _ in range(m)]
dp = [0] * (n + 1)
broken = [False] * (n + 1)
dp[0] = 1
for a in A:
  broken[a] = True
if broken[1] == False:
  dp[1] = 1
for i in range(2,n + 1):
  if broken[i] == False:
    dp[i] = dp[i - 2] + dp[i - 1]
print(dp[n] % mod)