n = int(input())
a = list(map(int,input().split()))
wild_cnt = 0
colors = []
for i in a:
  if 1 <= i <= 399:
    colors.append("g")
  elif 400 <= i <= 799:
    colors.append("br")
  elif 800 <= i <= 1199:
    colors.append("gr")
  elif 1200 <= i <= 1599:
    colors.append("wa")
  elif 1600 <= i <= 1999:
    colors.append("bl")
  elif 2000 <= i <= 2399:
    colors.append("y")
  elif 2400 <= i <= 2799:
    colors.append("o")
  elif 2800 <= i <= 3199:
    colors.append("r")
  elif 3200 <= i:
    wild_cnt += 1
# 3200以上しか存在しない場合
if len(set(colors)) == 0:
  print(str(1) + " " + str(min(n,wild_cnt)))
else:
  print(str(len(set(colors)))+ " " +str(min(n,len(set(colors)) + wild_cnt)))