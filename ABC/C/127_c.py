n,m = map(int,input().split())
conditions = [ tuple(map(int,input().split())) for _ in range(m)]
max_l = 0
min_r = float("INF")
for l,r in conditions:
  max_l = max(max_l,l)
  min_r = min(min_r,r)
if min_r < max_l:
  print(0)
else:
  print(min_r - max_l + 1)