n,x = map(int,input().split())
l = list(map(int,input().split()))
ans = 1
line = 0
for i in range(n):
  line += l[i]
  if line <= x:
    ans += 1
  else:
    break
print(ans)