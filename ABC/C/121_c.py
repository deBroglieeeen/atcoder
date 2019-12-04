n,m = map(int,input().split())
drink = [list(map(int,input().split())) for _ in range(n)]
s_drink = sorted(drink,key=lambda x:x[0])
ans = 0
count = 0
for i in range(n):
  if s_drink[i][1] + count > m:
    ans += s_drink[i][0] * (m - count)
    count += (m - count)
    break
  else:
    ans += s_drink[i][0] * s_drink[i][1]
    count += s_drink[i][1]
print(ans)