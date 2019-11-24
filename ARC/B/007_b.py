n,m =map(int,input().split())
disk = [int(input()) for _ in range(m)]
player = 0
case = []
for i in range(1,n + 1):
  case.append(i)
for i in range(m):
  if disk [i] == player:
    continue
  else:
    index = case.index(disk[i])
    case[index] = player
    player = disk[i]
for d in case:
  print(d)