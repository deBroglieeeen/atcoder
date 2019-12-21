n = int(input())
a = list()
xy = list()
for i in range(n):
  A = int(input())
  XY = [tuple(map(int,input().split())) for i in range(A)]
  a.append(A)
  xy.append(XY)
is_paradox = False
ans = 0
for i in range(2 ** n):
  honest = []
  for j in range(n):
    if i >> j & 1:
      honest.append(1)
    else:
      honest.append(0)
  for k,v in enumerate(a):
    if honest[k] == 0:
      continue
    for x,y in xy[k]:
      x -= 1
      if y == 1 and honest[x] != 1:
        is_paradox = True
        break
      elif y == 0 and honest[x] == 1:
        is_paradox = True
        break
  if is_paradox:
    is_paradox = False
    continue
  if is_paradox == False:
    ans = max(ans,sum(honest))
print(ans)