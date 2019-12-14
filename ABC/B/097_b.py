import math
x = int(input())
exp = set()
# for i in range(x,0,-1):
#   if math.sqrt(i).is_integer():
#     print(i)
#     break
for b in range(1,x + 1):
  for p in range(2,int(math.log2(x)) + 1):
    if b ** p <= x:
      exp.add(b ** p)
if len(exp) == 0:
  print(1)
else:
  print(max(exp))