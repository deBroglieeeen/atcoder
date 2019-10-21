from itertools import*
n,m = map(int,input().split())
faction = [[0]*n for _ in range(n)]
ans = 1
#行をx列をyとした議員同士が知り合いであるかを表すn*nの表を作成
for _ in range(m):
  x,y = map(int,input().split())
  faction[x-1][y-1] = 1
  faction[y-1][x-1] = 1
for i in range(2**n):
  ids = []
  for j in range(n):
    if i >> j & 1:
     ids.append(j)
  if all(faction[x][y] for x,y in combinations(ids,2)):
    if ans < len(ids):
      ans = len(ids)
print(ans)