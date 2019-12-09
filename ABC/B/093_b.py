a,b,k = map(int,input().split())
t = range(a,b+1)
if k > len(t):
  for i in t:
    print(i)
else:
  ls = []
  for i in range(k):
    ls.append(t[i])
  for i in range(k):
    ls.append(t[-i -1])
  ls = sorted(set(ls))
  for s in ls:
    print(s)