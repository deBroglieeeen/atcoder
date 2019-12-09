n,t = map(int,input().split())
routes = [list(map(int,input().split())) for _ in range(n)]
routes = sorted(routes,key=lambda x:x[0])
ans = "TLE"
for i in range(n):
  if routes[i][1] <= t:
    ans = str(routes[i][0])
    break
print(ans)