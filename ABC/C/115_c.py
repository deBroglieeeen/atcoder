n,k = map(int,input().split())
H = sorted([int(input()) for _ in range(n)])
ans = float("INF")
for i in range(n - k + 1):
  diff = H[k + i -1] - H[i]
  ans = min(ans,diff)
print(ans)