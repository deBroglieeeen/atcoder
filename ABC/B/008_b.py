import collections
n = int(input())
S = [input() for _ in range(n)]
stat = collections.Counter(S)
c_v = 0
ans = ""
for k,v in stat.items():
  if c_v < v:
    c_v = v
    ans = k
print(ans)