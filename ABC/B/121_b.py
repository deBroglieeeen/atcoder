n,m,c = map(int,input().split())
b = list(map(int,input().split()))
a = [list(map(int,input().split()))for _ in range(n)]
ans = 0
total = 0
for i in range(n):
  for j in range(m):
    if j == m - 1:
      total += a[i][j] * b[j]
      total += c
      if total > 0:
        ans += 1
      total = 0
    else:
      total += a[i][j] * b[j]
print(ans)