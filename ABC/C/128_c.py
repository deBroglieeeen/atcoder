n,m = map(int,input().split())
conditions = [tuple(map(int,input().split())) for _ in range(m)]
P = tuple(map(int,input().split()))
ans = 0
impossible = False
for i in range(2 ** n):
  switches = []
  for j in range(n):
    if i >> j & 1:
      switches.append(1)
    else:
      switches.append(0)
  for l in range(m):
    s_cnt = 0
    for s_needed in range(conditions[l][0]):
      s = conditions[l][s_needed + 1]
      if switches[s - 1] == 1:
        s_cnt += 1
    #if s_cnt == 0 or s_cnt % 2 != P[l]:
    if s_cnt % 2 != P[l]:
      impossible =True
      break
  if impossible:
    impossible = False
    continue
  ans += 1
  #print(switches)
print(ans)