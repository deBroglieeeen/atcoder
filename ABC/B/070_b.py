a,b,c,d = map(int,input().split())
ans = 0
al = range(a,b + 1)
bo = range(c,d + 1)
for l in al:
  if l in bo:
    ans += 1
if ans > 0:
  print(ans - 1)
else:
  print(0)