a,b = map(int,input().split())
ans = 0
for i in range(2):
  ans += max(a,b)
  if a > b:
    a -= 1
  else:
    b -= 1
print(ans)