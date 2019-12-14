m = int(input())
dist = m / 1000
vv = ""
if dist < 0.1:
  vv = "00"
elif 0.1 <= dist <= 5:
  vv = str(int(dist * 10))
elif 6 <= dist <= 30:
  vv = str(int(dist + 50))
elif 35 <= dist <= 70:
  vv = str(int((dist - 30) / 5 + 80))
elif dist > 70:
  vv = str(int(89))
if len(vv) == 1:
  print("0" + vv)
else:
  print(vv)