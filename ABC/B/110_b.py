n,m,x,y = map(int,input().split())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))
ans = "War"
for i in range(x + 1,y - x + x + 1):
  if max(X) < i and min(Y) >= i:
    ans = "No War"
print(ans)