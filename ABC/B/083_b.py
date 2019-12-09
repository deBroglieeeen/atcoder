n,a,b = map(int,input().split())
l = []
for i in range(1,n + 1):
  il = list(map(int,list(str(i))))
  if a <= sum(il) <= b:
    l.append(i)
print(sum(l))