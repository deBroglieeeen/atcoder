n,a,b = map(int,input().split())
comand = [list(input().split()) for _ in range(n)]
place = 0
for i in range(n):
  if comand[i][0] == "East":
    comand_dist = int(comand[i][1])
    if comand_dist < a:
      place += a
    elif comand_dist > b:
      place += b
    else:
      place += comand_dist
  else:
    comand_dist = int(comand[i][1])
    if comand_dist < a:
      place -= a
    elif comand_dist > b:
      place -= b
    else:
      place -= comand_dist
if place == 0:
  print(0)
elif place > 0:
  print("East",abs(place))
else:
  print("West",abs(place))