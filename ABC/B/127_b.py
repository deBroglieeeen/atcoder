r,d,x = map(int,input().split())
ans = 0
for i in range(10):
  if i == 0:
    ans = r * x -d
    print(ans)
  else:
    ans = r * ans - d
    print(ans)