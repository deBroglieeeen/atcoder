n = int(input())
a,b = map(int,input().split())
k = int(input())
P = list(map(int,input().split()))
route = set([a,b])
for p in P:
  route.add(p)
if len(route) == k + 2:
  print("YES")
else:
  print("NO")