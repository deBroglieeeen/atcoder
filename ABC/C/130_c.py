w,h,x,y = map(int,input().split())
print((w-0)*(h-0)/2)
if (w - 0)/2 == x and (h - 0)/2 == y:
  print(1)
else:
  print(0)
# vart = 0
# hori = 0
# vart = min((x - 0)*(h-0),(w - x)*(h - 0))
# hori = min((w - 0)*(y - 0),(w - 0)*(h - y))
# print(max(vart,hori))
# if vart == hori:
#   print(1)
# else:
#   print(0)