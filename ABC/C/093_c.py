a,b,c = sorted(map(int,input().split()))
if a % 2 == b % 2:
  d1 = (b - a) // 2
  d2 = c - b
  print(d1 + d2)
else:
  d1 = (b - a) // 2
  d1 += 1
  d2 = c - b
  d2 += 1
  print(d1 + d2)