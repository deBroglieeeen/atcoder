import itertools
n = int(input())
S = "MARCH"
d = {s:0 for s in S}
ans = 0
for i in range(n):
  f = input()[0]
  if f in S:
    d[f] += 1
for x,y,z in itertools.combinations(d.keys(),3):
  ans += d[x] * d[y] * d[z]
print(ans)