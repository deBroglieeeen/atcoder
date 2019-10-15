a,b = map(int,input().split())
k = 0
if a > b:
  k = a - b
  if k % 2 != 0:
    print('IMPOSSIBLE')
  else:
    print(int((k/2)+b))
else:
  k = b - a
  if k % 2 != 0:
    print('IMPOSSIBLE')
  else:
    print(int((k/2)+a))