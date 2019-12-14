n,m = map(int,input().split())
if n > 12:
  n -= 12
deg_n = 30 * n + 0.5 * m
deg_m = 6 * m
print(min(abs(deg_n - deg_m),360 - abs(deg_n - deg_m)))