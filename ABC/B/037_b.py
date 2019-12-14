n,q = map(int,input().split())
mani = [list(map(int,input().split())) for _ in range(q)]
line = [0] * n
for i in range(q):
  for j in range(mani[i][0] - 1,mani[i][1]):
    line[j] = mani[i][2]
    #print(mani[i][2])
for num in line:
  print(num)