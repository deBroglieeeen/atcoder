import collections
n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]
blue = collections.Counter(s)
red = collections.Counter(t)
for k_b,v_b in blue.items():
  for k_r,v_r in red.items():
    if k_b == k_r:
      blue[k_b] = v_b - v_r
if max(blue.values()) < 0:
  print(0)
else:
  print(max(blue.values()))