import collections
n,m = map(int,input().split())
problems = [tuple(input().split()) for _ in range(m)]
#print(collections.Counter(problems))
alist = []
wlist = []
ac_counter = 0
wa_counter = 0
for _ in range(m):
  t = tuple(input().split())
  checkac = (t[0],"AC")
  if t[1] == "WA" and not checkac in alist:
    #alist.append(t)
    wa_counter += 1
  elif t[1] == "AC" and not checkac in alist:
    alist.append(t)
    ac_counter += 1
#print(collections.Counter(alist))
#for c,r in collections.Counter(alist)
print(ac_counter,wa_counter)