import math
s = list(input().split())
con = "".join(s)
if math.sqrt(int(con)).is_integer():
  print("Yes")
else:
  print("No")