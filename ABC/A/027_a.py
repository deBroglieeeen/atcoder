import collections
d = collections.Counter(list(map(int,input().split())))
mi = min(d.values())
for k,v in d.items():
  if v == mi:
    print(k)
    break