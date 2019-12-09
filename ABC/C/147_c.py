n = int(input())
a = list()
xy = list()
for i in range(n):
  A = int(input())
  XY = [tuple(map(int,input().split())) for i in range(A)]
  a.append(A)
  xy.append(XY)
ans = 0
for i in range(2 ** n-1,-1,-1):
  mini_ans = 0
  honest = []
  for j in range(n):
    honest.append(i % 2)
    i = i // 2
  for k,v in enumerate(honest):
    if v:
      mini_ans += 1
      for x,y in xy[k]:
        x -= 1
        if honest[x] != y:
          break
        else:
          continue
        break
    else:
      ans = max(ans,mini_ans)
      continue
print(ans)