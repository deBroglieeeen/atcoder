from collections import defaultdict
n,m = map(int,input().split())
d = defaultdict(list)
l = [0] * m
for i in range(m):
  p,y = map(int,input().split())
  d[p].append((y,i))
for k,cities in d.items():
  cities.sort()
  for j in range(len(cities)):
    _,i = cities[j]
    l[i] = "0" * (6 - len(str(k))) + str(k) + "0" * (6 - len(str(j + 1))) + str(j + 1)
print(*l,sep="\n")