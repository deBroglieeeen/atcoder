n,x = map(int,input().split())
if abs(n - x) < abs(x - 1):
  print(n - x)
else:
  print(x - 1)