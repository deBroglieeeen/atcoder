w,a,b = map(int,input().split())
# dis = b - (w + a)
# if dis <= 0:
#   print(0)
# else:
#   print(dis)
if a > b:
  dis = a - (w + b)
  if dis <= 0:
    print(0)
  else:
    print(dis)
else:
  dis = b - (w + a)
  if dis <= 0:
    print(0)
  else:
    print(dis)