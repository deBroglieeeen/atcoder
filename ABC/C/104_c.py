d,g = map(int,input().split())
p = [list(map(int,input().split())) for i in range(d)]
ans = float('inf')
for i in range(2**d):
  solved = 0
  point = 0
  luck = -1
  for j in range(d):
    if i >> j & 1:
      # pi問題をすべてといた場合の得点を加算
      point += 100 * (j+1) * p[j][0] + p[j][1]
      solved += p[j][0]
    #elif luck < 0:
    else:
      luck = j
  #全問とかないようにするため
  k = 0
  # 不完全解答するのは最も配点が高い大問1第のみ
  while k < p[luck][0] and point < g:
    point += 100 * (luck + 1)
    k += 1
    solved += 1
  if point >= g and solved < ans:
    ans = solved
print(ans)
