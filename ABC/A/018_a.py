a = int(input())
b = int(input())
c = int(input())
l = sorted([a,b,c],reverse=True)
for k in [a,b,c]:
  print(l.index(k)+1)