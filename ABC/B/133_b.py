import math
n,d = map(int,input().split())
x = [list(map(int,input().split())) for i in range(n)]
norm = 0
ans = 0
for i in range(n - 1):
  for j in range(i+1,n):
    for k in range(d):
      norm += abs(x[i][k]-x[j][k])**2
      if k == (d - 1):
        p = math.sqrt(norm)
        norm = 0
        if p.is_integer():
          ans += 1
print(ans)