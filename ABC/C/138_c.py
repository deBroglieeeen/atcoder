n = int(input())
v = list(map(int,input().split()))
values = []
v = sorted(v)
pot = v[0]
for i in range(n - 1):
  pot = (pot + v[i + 1]) / 2
  if i == n - 2:
    values.append(pot)
print(max(values))