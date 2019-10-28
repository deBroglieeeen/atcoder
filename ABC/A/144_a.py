a,b = map(int,input().split())
if a > 9 or b > 9:
  print(str(-1))
else:
  print(str(a * b))