n = int(input())
v = list(map(int,input().split()))
c = list(map(int,input().split()))
ans = 0
# for i in range(2**n):
#   x = []
#   y = []
#   for j in range(n):
#     if (i>>j) & 1:
#       x.append(v[n - j - 1])
#       y.append(c[n - j - 1])
#   ans = max(ans,sum(x) - sum(y))
for i in range(n):
  if v[i] > c[i]:
    ans += v[i] - c[i]
print(ans)