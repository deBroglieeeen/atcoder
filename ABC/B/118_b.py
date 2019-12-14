import collections
n,m = map(int,input().split())
h = []
for i in range(n):
  h[len(h):len(h)] = list(map(int,input().split()))[1:]
ans = 0
count = collections.Counter(h)
for v in count.values():
  if v == n:
    ans += 1
print(ans)