n = int(input())
q = list(range(1,n+1))
p = map(int,input().split())
difCount = 0
for i,j in zip(p,q):
  if i != j:
    difCount+=1
if difCount <= 2:
  print('YES')
else:
  print('NO')